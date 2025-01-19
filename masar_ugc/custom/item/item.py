import frappe
import json
import requests
def validate(self, method):
    set_shortdisc(self)
    publish_to_web(self)
    insert_item_to_asp(self)
    update_item_in_asp(self)

def set_shortdisc(self):
    if self.custom_short_disc_en:
        self.description = self.custom_short_disc_en
        

def publish_to_web(self):
    if self.workflow_state == "Publish":
        self.custom_is_publish = 1
        if self.custom_is_publish:
            frappe.msgprint(f"Item: {self.name}, is published", alert=True, indicator="green")
    else:
        self.custom_is_publish = 0
        
        
def get_payload_data(self):
        data = { 
            "ItemCode": self.item_code, 
            "ItemName": self.item_name, 
            "CategoryEN": self.custom_category_en, 
            "CategoryAR": self.custom_category_ar, 
            "CategoryFR": self.custom_category_fr, 
            "BrandEN": self.custom_brand_en, 
            "BrandAR": self.custom_brand_ar, 
            "BrandFR": self.custom_brand_fr, 
            "SubBrand1EN": self.custom_subbrand1_en, 
            "SubBrand1AR": self.custom_subbrand1_ar, 
            "SubBrand1FR": self.custom_subbrand1_fr, 
            "SubBrand2EN": self.custom_subbrand2_en, 
            "SubBrand2AR": self.custom_subbrand2_ar, 
            "SubBrand2FR": self.custom_subbrand2_fr, 
            "SubBrandPic": self.custom_subbrand_pic_en, 
            "SubBrandVed": self.custom_subbrand_ved_en, 
            "ShortDescriptionEN": self.custom_short_disc_en, 
            "ShortDescriptionAR": self.custom_short_disc_ar, 
            "ShortDescriptionFR": self.custom_short_disc_fr, 
            "DescriptionEN": self.custom_long_disc_en, 
            "DescriptionAR": self.custom_long_disc_ar, 
            "DescriptionFR": self.custom_long_disc_fr, 
            "ProductUseEN": self.custom_product_use_en, 
            "ProductUseAR": self.custom_product_use_ar, 
            "ProductUseFR": self.custom_product_use_fr, 
            "Surface1EN": self.custom_surface1_en, 
            "Surface1AR": self.custom_surface1_ar, 
            "Surface1FR": self.custom_surface1_fr, 
            "Surface2EN": self.custom_surface2_en, 
            "Surface2AR": self.custom_surface2_ar, 
            "Surface2FR": self.custom_surface2_fr, 
            "Surface3EN": self.custom_surface3_en, 
            "Surface3AR": self.custom_surface3_ar, 
            "Surface3FR": self.custom_surface3_fr, 
            "FinishesEN": self.custom_finishes_en, 
            "FinishesAR": self.custom_finishes_ar, 
            "FinishesFR": self.custom_finishes_fr, 
            "Colors": self.custom_colors_en, 
            "MSDS": self.custom_msds_en, 
            "TDS": self.custom_tds_en, 
            "Sheen": self.custom_sheen_en, 
            "MetaDescriptionEN": self.custom_metadisc_en, 
            "MetaDescriptionAR": self.custom_metadisc_ar, 
            "MetaDescriptionFR": self.custom_metadisc_fr, 
            "CoveragePerPackEN": self.custom_coverageperpack_en, 
            "CoveragePerPackAR": self.custom_coverageperpack_ar, 
            "CoveragePerPackFR": self.custom_coverageperpack_fr, 
            "ApplicationToolEN": self.custom_applicationtool_en, 
            "ApplicationToolAR": self.custom_applicationtool_ar, 
            "ApplicationToolFR": self.custom_applicationtool_fr, 
            "PackSizeEN": self.custom_packsize_en, 
            "PackSizeAR": self.custom_packsize_ar, 
            "PackSizeFR": self.custom_packsize_fr
        }
def get_header_data():
    return  {
  'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
  'Content-Type': 'application/json'}
def insert_item_to_asp(self):
    if self.custom_inserted_to_asp == 0: 
        url = "https://demo.es.jo/ugsASP/UGCInsertProduct.ashx"
        response = requests.request("POST", url, headers=get_header_data(), data=json.dumps(get_payload_data(self)))
        if response.status_code == 200:
            frappe.msgprint(f'Item {self.name} is Created Successfully in ASP.' , alert=True , indicator='green')
            self.custom_inserted_to_asp = 1 
            

def update_item_in_asp(self):
    if self.custom_inserted_to_asp == 1: 
        url = "https://demo.es.jo/ugsASP/UGCEditProduct.ashx"
        response = requests.request("POST", url, headers=get_header_data(), data=json.dumps(get_payload_data(self)))
        if response.status_code == 200:
            frappe.msgprint(f'Item {self.name} is updated Successfully in ASP.' , alert=True , indicator='green')