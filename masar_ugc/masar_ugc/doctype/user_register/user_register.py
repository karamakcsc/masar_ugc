# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class UserRegister(Document):
# 	pass


# @frappe.whitelist()
# def createdoc(you_are , first_name_en, middle_name_en, last_name_en, register_date, email):

#     doc_user = frappe.new_doc('User')
#     doc_user.email = email 
#     doc_user.first_name = first_name_en
#     doc_user.middle_name = middle_name_en
#     doc_user.last_name = last_name_en
#     doc_user.full_name = f"{first_name_en} {middle_name_en} {last_name_en}"
#     doc_user.insert(ignore_permissions = True)
#     doc_user.save()
#     if you_are == "موظف":
#         ##### create employee 
#         doc_emplyee = frappe.new_doc('Employee')
#         doc_emplyee.first_name = first_name_en
#         doc_emplyee.middle_name = middle_name_en
#         doc_emplyee.last_name = last_name_en
#         doc_emplyee.date_of_joining = register_date
#         doc_emplyee.user_id = email
#         doc_emplyee.gender = "Male"
#         doc_emplyee.date_of_birth = register_date
#         doc_emplyee.insert(ignore_permissions = True)
#         doc_emplyee.save()
#     elif you_are == "عميل":
#         doc_customer = frappe.new_doc('Customer')
#         doc_customer.customer_name = f"{first_name_en} {middle_name_en} {last_name_en}"
#         doc_customer.insert(ignore_permissions = True)
#         doc_customer.save()
#     return f"The {you_are} is Created "

################################################################################################

# import frappe
# from frappe.model.document import Document

# class UserRegister(Document):
# 	pass

# @frappe.whitelist()
# def createdoc(you_are , first_name_en, middle_name_en, last_name_en, register_date, email):
#     doc_user = frappe.new_doc('User')
#     doc_user.email = email 
#     doc_user.first_name = first_name_en
#     doc_user.middle_name = middle_name_en
#     doc_user.last_name = last_name_en
#     doc_user.full_name = "{} {} {}".format(first_name_en, middle_name_en, last_name_en)
#     doc_user.insert(ignore_permissions = True)
#     doc_user.save()
#     if you_are == "موظف":
#         doc_emplyee = frappe.new_doc('Employee')
#         doc_emplyee.first_name = first_name_en
#         doc_emplyee.middle_name = middle_name_en
#         doc_emplyee.last_name = last_name_en
#         doc_emplyee.date_of_joining = register_date
#         doc_emplyee.user_id = email
#         doc_emplyee.gender = "Male"
#         doc_emplyee.date_of_birth = register_date
#         doc_emplyee.insert(ignore_permissions = True)
#         doc_emplyee.save()
#     elif you_are == "عميل":
#         doc_customer = frappe.new_doc('Customer')
#         doc_customer.customer_name = "{} {} {}".format(first_name_en, middle_name_en, last_name_en)
#         doc_customer.insert(ignore_permissions = True)
#         doc_customer.save()
#     return "The {} is Created ".format(you_are)

   
################################################################################################

# @frappe.whitelist()
# def createdoc(you_are , first_name_en, middle_name_en, last_name_en, register_date, email):
    
#     doc_user = frappe.new_doc('User')
#     doc_user.email = email 
#     doc_user.first_name = first_name_en
#     doc_user.middle_name = middle_name_en
#     doc_user.last_name = last_name_en
#     doc_user.full_name = f"{first_name_en} {middle_name_en} {last_name_en}"
#     doc_user.insert(ignore_permissions = True)
#     doc_user.save()
#     if you_are == "موظف":
#         doc_emplyee = frappe.new_doc('Employee')
#         doc_emplyee.first_name = first_name_en
#         doc_emplyee.middle_name = middle_name_en
#         doc_emplyee.last_name = last_name_en
#         doc_emplyee.date_of_joining = register_date
#         doc_emplyee.user_id = email
#         doc_emplyee.gender = "Male"
#         doc_emplyee.date_of_birth = register_date
#         doc_emplyee.insert(ignore_permissions = True)
#         doc_emplyee.save()
#     elif you_are == "عميل":
#         doc_customer = frappe.new_doc('Customer')
#         doc_customer.customer_name = f"{first_name_en} {middle_name_en} {last_name_en}"
#         doc_customer.insert(ignore_permissions = True)
#         doc_customer.save()
#     return f"The {you_are} is Created " 

################################################################################################

#     # email_sql = frappe.db.sql("""SELECT email FROM tabUser Register """ , as_dict = True)
#     # email_lst = [item["email"] for item in email_sql]
#     # frappe.msgprint((str(email_lst)))
#     # if str(email) in email_lst:
#     #     frappe.msgprint("User Already Exist.")
#     #     return  0
#     # return  1 