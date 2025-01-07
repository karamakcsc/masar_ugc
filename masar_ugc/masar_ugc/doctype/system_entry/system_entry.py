# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SystemEntry(Document):
    @frappe.whitelist()
    def get_max_system_no(self):
        if self.system_brand:
            max_no_sql = frappe.db.sql(
                """
					SELECT MAX(tse.system_no) 
					FROM `tabSystem Entry` tse 
					WHERE  tse.system_brand = %s
				""", (self.system_brand))
            if not max_no_sql or not max_no_sql[0] or not max_no_sql[0][0]:
                if self.system_brand == 'Jotun':
                    return 2201  # 2200+1
                elif self.system_brand == 'Uniguard':
                    return 1101  # 1100+1
                elif self.system_brand == 'Jotun&Uniguard':
                    return 3001  # 3000+1
            else:
                max_no = max_no_sql[0][0]
                return max_no + 1

        return None
