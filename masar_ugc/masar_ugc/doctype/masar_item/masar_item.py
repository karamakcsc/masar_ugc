# Copyright (c) 2025, KCSC and contributors
# For license information, please see license.txt

import frappe
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
                    item_data = {
						"item_name": data.get("item_name"),
						"item_group": data.get("item_group"),
						# "custom_item_name_ar": data.get("item_name_ar"),
						# "custom_short_disc_en": data.get("short_disc_en"),
						# "custom_short_disc_ar": data.get("short_disc_ar"),
						"custom_solid_content": data.get("solid_content"),
						"custom_spreading_rate": data.get("spreading_rate", 0),
						"custom_dft_desc": data.get("dft_desc")
					}
                    if frappe.db.exists("Item", item_code):
                        item = frappe.get_doc("Item", item_code)
                        item.update(item_data)
                        item.save()
                        frappe.db.set_value(data.doctype , data.name ,'response', f"Item {item_code} updated successfully")
                    else:
                        new_item = frappe.new_doc("Item")
                        new_item.item_code = item_code
                        new_item.update(item_data)
                        new_item.insert()
                        frappe.db.set_value(data.doctype , data.name ,'response', f"Item {item_code} Updated successfully")   
                except Exception as e:
                    frappe.db.set_value(data.doctype , data.name ,'response', f"Error processing item {item_code}: {str(e)}")
                   
            