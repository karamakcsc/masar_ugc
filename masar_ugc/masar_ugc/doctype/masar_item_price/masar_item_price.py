# Copyright (c) 2025, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MasarItemPrice(Document):
    def on_submit(self):
        frappe.enqueue(self.create_and_update_item_prices, queue='long', timeout=6000)
        
    def create_and_update_item_prices(self):		
        for data in self.items:
            try:
                if frappe.db.exists("Price List", data.pl_voutype_desc):
                    price_list = frappe.get_doc("Price List", data.pl_voutype_desc)
                else:
                    price_list = frappe.new_doc("Price List")
                    price_list.price_list_name = data.pl_voutype_desc
                    price_list.currency = "JOD"
                    price_list.selling = 1
                    price_list.buying = 0
                    price_list.insert()
                if frappe.db.exists("Item Price", {"item_code": data.item_code, "price_list": data.pl_voutype_desc , "price_list_rate": data.item_price}):
                    frappe.db.set_value(data.doctype , data.name ,'response', f"Item Price for Item {data.item_code} in Price List {data.pl_voutype_desc} already exists")
                else:
                    item_price = frappe.new_doc("Item Price")
                    item_price.item_code = data.item_code
                    item_price.price_list = data.pl_voutype_desc
                    item_price.price_list_rate = data.item_price
                    item_price.insert()
                    frappe.db.set_value(data.doctype , data.name ,'response', f"Item Price for Item {data.item_code} in Price List {data.pl_voutype_desc} created successfully")
            except Exception as e:
                frappe.db.set_value(data.doctype , data.name ,'response', f"Error processing item price for item {data.item_code} in Price List {data.pl_voutype_desc}: {str(e)}")
     