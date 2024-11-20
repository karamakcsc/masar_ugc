# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Header(Document):
	def validate(self):
		self.side_vaildate()
		self.defualt_validate()
     
	def side_vaildate(self):	
		if (self.left_header + self.right_header) !=1:
				frappe.throw(
					'Please select either the left or right side for the header. Both sides cannot be selected simultaneously.',
					title = frappe._("Validation Error")
				)
	def defualt_validate(self): 
		if self.is_enable: 
			if self.defualt and self.left_header: 
				q = frappe.qb.DocType(self.doctype)
				exist = (
        			frappe.qb.from_(q)
           				.select(q.name)
               			.where(q.defualt ==1 )
						.where(q.is_enable ==1 )
						.where(q.left_header ==1 )
						.where(q.name != self.name )
                ).run()
				if exist and exist[0] and exist[0][0]:
					frappe.throw(
						'Only One Left Header Set as Defualt. Aleady Exist in {ex}'.format(ex =exist[0][0] )
					)
			if self.defualt and self.right_header: 
				q = frappe.qb.DocType(self.doctype)
				exist = (
        			frappe.qb.from_(q)
           				.select(q.name)
               			.where(q.defualt ==1 )
						.where(q.is_enable ==1 )
						.where(q.right_header ==1 )
						.where(q.name != self.name )
                ).run()
				if exist and exist[0] and exist[0][0]:
					frappe.throw(
						'Only One Right Header Set as Defualt. Aleady Exist in {ex}'.format(ex =exist[0][0] )
					)