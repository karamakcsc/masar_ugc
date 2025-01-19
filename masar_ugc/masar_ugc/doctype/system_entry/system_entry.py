# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json
import requests
from masar_ugc.api import get_header_data
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
    def validate(self): 
        self.system_master_asp_api()
        
    def get_payload_data(self):
        system_items = list()
        
        for i in self.
        return { 
                "SystemID": self.name,
            "SystemNo": self.system_no,
            "SystemNameEN": self.system_name_en,
            "SystemNameAR": self.system_name_ar,
            "SystemNameFR": self.system_name_fr,
            "AreaofUseEN": self.sub_area_of_use_en,
            "AreaofUseAR": self.sub_area_of_use_ar,
            "AreaofUseFR": self.sub_area_of_use_fr,
           "AreaofUseEN2": self.area_of_use_en_2,
            "AreaofUseAR2": self.area_of_use_ar_2,
            "AreaofUseFR2": self.area_of_use_fr_2,
            "AreaofUseEN3": self.area_of_use_en_3,
            "AreaofUseAR3": self.area_of_use_ar_3,
            "AreaofUseFR3": self.area_of_use_fr_3,
            "SystemBrand": self.system_brand,
            "SystemImageLink": self.system_image_link,
            "SystemBodyImageLink": f"https://ugc.kcsc.com.jo{self.body_image}", ##################################
            "SystemVideoLink": self.system_video_link,
            "SystemTestResultLink": self.test_result_link,
            "SystemStatementLink": self.statement_link,
            "SystemDescriptionEN": self.system_metadisc_en,
            "SystemDescriptionAR": self.system_metadisc_ar,
            "SystemDescriptionFR": self.system_metadisc_fr,
            "MetaDescriptionEN": self.system_description_en,
            "MetaDescriptionAR": self.system_description_ar,
            "MetaDescriptionFR": self.system_description_fr,
            "Publish":self.is_published,
            "SystemItems": [
                {
                    "ItemCode": "03-02-11-01-0008",
                    "idx": 1,
                    "ProductUseEN": "Product Use EN",
                    "ProductUseAR": "استخدام المنتج AR",
                    "ProductUseFR": "Utilisation du produit FR",
                    "ProductNoOfCoatsEN":"2 Coats",
                    "ProductNoOfCoatsAR": "2 طبقات",
                    "ProductNoOfCoatsFR": "2 couches",
                    "ProductSubBrand2EN": "Product Description EN",
                    "ProductSubBrand2AR": "وصف المنتج AR",
                    "ProductSubBrand2FR": "Description du produit FR"
                }
            ]
        }

    def system_master_asp_api(self): 
        "check if existing in ASP"
        url = f"https://demo.es.jo/ugsASP/UGCSelectSystem.ashx?SystemNo={self.system_no}"
        response = requests.request("GET", url, headers=get_header_data(), data={})
        if response.status_code == 200: 
            self.update_system_master()
        else: 
            self.insert_system_master()
            
    def insert_system_master(self): 
        