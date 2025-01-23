# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
from masar_ugc.api import get_base_url , get_header_data

class Category(Document):
	def validate(self):
		if self.is_enabled: 
			self.category_api()
	def category_api(self):
		url = f'{get_base_url()}UGCCatMeta.ashx'
		payload =  {
      			"CategoryEN": self.category_name_en,
         		"CategoryAR":self.category_name_ar,
           		"CategoryFR":self.category_name_fr,
             	"MetaDiscEN":self.category_meta_disc_en,
              	"MetaDiscAR": self.category_meta_disc_ar,
               	"MetaDiscFR": self.category_meta_disc_fr
        }
		try:
			response = requests.post(url, headers=get_header_data(), data=payload)
			if response.status_code == 200:
				frappe.msgprint(f'Category {self.name} Successfully Inserted/Updated in ASP', alert=True, indicator='green')
			else:
				frappe.throw(f"Update Category failed: {str(response.text)}")
		except requests.RequestException as e:
			frappe.throw(f"Request failed: {str(e)}")