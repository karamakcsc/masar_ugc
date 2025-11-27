# Copyright (c) 2025, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt
from frappe.model.document import Document

class MasarItem(Document):
    def on_submit(self):
        frappe.enqueue(self.create_and_update_items, queue='long', timeout=20000)

    def create_and_update_items(self):        
        for data in self.items:
            if data.to_reflect:
                try:
                    item_code = data.item_code
                    if not item_code:
                        frappe.db.set_value(data.doctype , data.name ,'response', "Item code is missing")
                        continue
                    packsize = data.unit_content if data.unit_content else 0
                    if packsize:
                        if not frappe.db.exists("Pack Size", packsize):
                            new_packsize = frappe.get_doc({
                                "doctype": "Pack Size",
                                "pack_size_en": packsize,
                                "enabled": 1
                            })
                            new_packsize.insert(ignore_permissions=True)
                            frappe.db.commit()
                    item_data = {
						"item_name": data.get("item_name"),
						"item_group": data.get("item_group"),
						# "custom_item_name_ar": data.get("item_name_ar"),
						# "custom_short_disc_en": data.get("short_disc_en"),
						"custom_masar_id": str(data.get("masar_id")),
						"custom_solid_content": data.get("solid_content", 0),
						"custom_spreading_rate": flt(data.get("spreading_rate", 0), 3),
						"custom_dft_desc": data.get("dft_desc"),
                        "disabled": data.get("item_active", 0),
                        "weight_per_unit": data.get("item_weight", 0),
                        "weight_uom": "Kg",
                        "custom_packsize_en": packsize,
                        "custom_no_of_coats": data.get("no_of_coats", ""),
					}
                    if frappe.db.exists("Item", item_code):
                        item = frappe.get_doc("Item", item_code)
                        if item.uoms:
                            uoms = set()
                            unique_rows = []

                            for row in item.uoms:
                                if row.uom not in uoms:
                                    uoms.add(row.uom)
                                    unique_rows.append(row)

                            item.uoms = unique_rows
                                
                        item.update(item_data)
                        item.save()
                        frappe.db.set_value(data.doctype , data.name ,'response', f"Item {item_code} updated successfully")
                    else:
                        new_item = frappe.new_doc("Item")
                        new_item.item_code = item_code
                        new_item.update(item_data)
                        if new_item.uoms:
                            uoms = set()
                            unique_rows = []

                            for row in item.uoms:
                                if row.uom not in uoms:
                                    uoms.add(row.uom)
                                    unique_rows.append(row)

                            new_item.uoms = unique_rows
                        new_item.insert()
                        frappe.db.set_value(data.doctype , data.name ,'response', f"Item {item_code} Updated successfully") 
                except Exception as e:
                    frappe.db.set_value(data.doctype , data.name ,'response', f"Error processing item {item_code}: {str(e)}")
        frappe.db.commit()            
            