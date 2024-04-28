# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.permissions import (
# 	add_user_permission,
# 	get_doc_permissions,
# 	has_permission,
# 	remove_user_permission,
# )
class UserRegister(Document):
    def on_submit(self):
        self.createdoc()
   
    def validate(self):
        self.fill_full_name()
    

    @frappe.whitelist()   
    def create_user(self):
        doc_user = frappe.new_doc('User')
        doc_user.email = str(self.email) 
        doc_user.first_name = self.first_name_en
        doc_user.middle_name = self.middle_name_en
        doc_user.last_name = self.last_name_en
        doc_user.insert(ignore_permissions=True)
        doc_user.enabled = 0 
        doc_user.save()
        frappe.db.commit()
        return f"Create User {self.first_name_en} {self.middle_name_en} {self.last_name_en}"
    

    def createdoc(self):
        if self.you_are == "موظف":
            entry = {
                'first_name' : self.first_name_en,
                'middle_name': self.middle_name_en , 
                'last_name' : self.last_name_en,
                'date_of_joining': self.register_date , 
                # 'full_name_en': f' {self.first_name_en} {self.middle_name_en} {self.last_name_en}',
                # 'user_id': self.email,
                'gender' : "Male",
                'date_of_birth': self.register_date
            }
            frappe.new_doc('Employee').update(entry).insert(ignore_permissions=True, ignore_mandatory=True)
            frappe.db.commit()

        elif self.you_are == "عميل":
            doc_customer = frappe.new_doc('Customer')
            doc_customer.customer_name = f"{self.first_name_en} {self.middle_name_en} {self.last_name_en}"
            # doc_customer.custom_number_of_doors = self.number_of_doors
            # doc_customer.custom_signboard_type = self.signboard_type
            # doc_customer.custom_customer_evaluation = self.customer_evaluation
            # doc_customer.custom_customer_sector = self.customer_sector
            doc_customer.insert(ignore_permissions=True)
            frappe.db.commit()

        elif self.you_are == "دهين":
            doc_painter = frappe.new_doc('Painter')
            doc_painter.first_name = self.first_name_en
            doc_painter.middle_name = self.middle_name_en
            doc_painter.last_name = self.last_name_en
            doc_painter.full_name = f"{self.first_name_en} {self.middle_name_en} {self.last_name_en}"
            doc_painter.mobile_number = self.mobile_no
            doc_painter.insert(ignore_permissions=True)
            frappe.db.commit()
        frappe.msgprint(f"The {self.you_are} is Created for {self.first_name_en} {self.middle_name_en} {self.last_name_en}") 


    def fill_full_name(self):
        self.full_name_en = f"{self.first_name_en} {self.middle_name_en} {self.last_name_en}"
        self.full_name_ar = f"{self.first_name_ar} {self.middle_name_ar} {self.last_name_ar}"

