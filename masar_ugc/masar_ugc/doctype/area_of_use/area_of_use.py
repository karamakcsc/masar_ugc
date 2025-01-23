# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from masar_ugc.api import get_header_data , get_base_url
import requests
import json
class AreaofUse(Document):
    def validate(self): 
        if self.is_enabled: 
            self.area_of_use_api()
   
    def area_of_use_api(self):
        url = f'{get_base_url()}UGCAreaofUse.ashx'
        payload = {
            "AreaofUseEN": self.area_of_use_en,
            "AreaofUseAR": self.area_of_use_ar,
            "AreaofUseFR": self.area_of_use_fr,
            "MetaDiscEN": self.area_of_use_metadiscen,
            "MetaDiscAR": self.area_of_use_metadiscar,
            "MetaDiscFR": self.area_of_use_metadiscfr
        }
        try:
            response = requests.post(url, headers=get_header_data(), data=json.dumps(payload))
            if response.status_code == 200:
                frappe.msgprint(f'Area of Use {self.name} Successfully Inserted/Updated in ASP', alert=True, indicator='green')
            else:
                frappe.throw(f"Update Area of Use failed: {str(response.text)}")
        except requests.RequestException as e:
            frappe.throw(f"Request failed: {str(e)}")

        
    