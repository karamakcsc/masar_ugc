# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PackSize(Document):
	def validate(self):
		uom_name = self.name

		if not frappe.db.exists("UOM", uom_name):
			uom = frappe.get_doc({
				"doctype": "UOM",
				"uom_name": uom_name,
				"enabled": 1
			})
			uom.insert(ignore_permissions=True)
			frappe.db.commit()
