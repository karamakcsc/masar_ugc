# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime, timedelta
from frappe.model.document import Document


class CustomersVisits(Document):
    
    def on_update(self):
        if not self.is_insert:
            self.child_row = self.insert_start_time()
        elif not self.is_closed_row:
            self.insert_end_time()

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
        if  self.status == 'Hold' or self.status =='Complete':
            try:
                row = frappe.get_doc('Customers Visits Details', {'parent': self.name})
                start_time = row.start_time
                end_time =  datetime.now()
                duration = (end_time - start_time).total_seconds()
                row.end_time = end_time
                row.duration = duration
                # row.location = 0           ##### current location 
                row.save()
                self.is_closed_row = 1
            except Exception as e:
                frappe.log_error(f"Error inserting end time: {str(e)}")
