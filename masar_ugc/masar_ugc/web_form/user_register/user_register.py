import frappe
from frappe import _
def get_context(context):
	# do your magic here
	pass


# @frappe.whitelist(allow_guest=True)
# def validate_user_email(email):
#     email_exists = frappe.db.sql("""SELECT email FROM `tabUser Register`""")
#     email_lst = [item["email"] for item in email_exists]
#     # frappe.msgprint(str(email_lst))
#     # if email in email_lst:
#     #     frappe.msgprint(_("Email already exists. Please choose a different one.python ")) 
#     return str(email_lst)
