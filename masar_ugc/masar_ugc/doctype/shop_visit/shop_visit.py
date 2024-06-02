# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class ShopVisit(Document):
	def on_update(self):
		if not self.is_insert:
			self.child_row = self.insert_start_time()
		elif not self.is_closed_row:
			self.insert_end_time()
		elif self.is_closed_row ==1 and self.is_insert==1:
			self.insert_event_row()
		
	def insert_start_time(self):
		try:
			user_id = frappe.session.user
			date_time_now = datetime.now()
			row = self.append('process_time_tab', {})
			row.start_time = date_time_now
			row.user_id = user_id
			self.is_insert = 1
		except Exception as e:
			frappe.log_error(f"Error inserting start time: {str(e)}")
			
	@frappe.whitelist()
	def insert_end_time(self):
		if self.status == 'Hold' or self.status =='Complete':
			try:
				self.is_closed_row = 1
				self.save()
				row = frappe.get_doc('Shop Visits Details', {'parent': self.name})
				start_time = row.start_time
				end_time_ =  datetime.now()
				duration = (end_time_ - start_time).total_seconds()
				row.end_time = end_time_
				row.duration = duration
				row.status = self.status
				row.save()
				frappe.db.commit()
			except Exception as e:
				frappe.log_error(f"Error inserting end time: {str(e)}")
	def insert_event_row(self):
		start_time = frappe.db.sql("""SELECT MAX(end_time) AS start_time FROM `tabShop Visits Details` tsvd """ , as_dict= True)[0]['start_time']
		end_time = datetime.now()
		if start_time and end_time:
			duration = (end_time - start_time).total_seconds()
		else: 
			duration = 0 
		user_id = frappe.session.user
		status = self.status 
		row = self.append('process_time_tab', {})
		row.user_id = user_id
		row.start_time = start_time
		row.end_time = end_time
		row.duration = duration
		row.status = status
		frappe.db.commit()

					