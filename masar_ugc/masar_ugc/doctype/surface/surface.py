# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from masar_ugc.api import get_base_url , get_header_data
import requests
class Surface(Document):
	def validate(self):
		if self.is_enabled: 
			self.surface_api()
   
	def surface_api(self):
		url = f"{get_base_url()}UGCSurfMeta.ashx"
		payload = {
      		"SurfaceEN": self.surface1_en,
        	"SurfaceAR": self.surface1_ar,
         	"SurfaceFR": self.surface1_fr,
          	"MetaDiscEN": self.surfacemetadiscen,
           	"MetaDiscAR": self.surfacemetadiscar,
            "MetaDiscFR": self.surfacemetadiscfr
        }
		try:
			response = requests.post(url, headers=get_header_data(), data=payload)
			if response.status_code == 200:
				frappe.msgprint(f'Surface {self.name} Successfully Inserted/Updated in ASP', alert=True, indicator='green')
			else:
				frappe.throw(f"Update Surface failed: {str(response.text)}")
		except requests.RequestException as e:
			frappe.throw(f"Request failed: {str(e)}")
