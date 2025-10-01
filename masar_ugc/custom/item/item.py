import frappe
import json
import requests
from masar_ugc.api import get_header_data , get_payload_data_for_item , get_base_url
def validate(self, method):
    set_shortdisc(self)
    publish_to_web(self)
    asp_item_api(self)

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
        
def asp_item_api(self):
    if self.disabled == 0 and  self.custom_visible == 1 and self.workflow_state == 'Publish': 
        publish = 1 
    else:
        publish = 0 
    if publish:
        url = f"{get_base_url()}UGCSelectProduct.ashx?ItemCode={self.item_code}"     
        response = requests.request("GET", url, headers=get_header_data(), data={})
        if response.status_code == 200: 
            update_item_in_asp(self ,publish ) 
        else: 
            insert_item_to_asp(self , publish)


def insert_item_to_asp(self , publish):
        url = f"{get_base_url()}UGCInsertProduct.ashx"
        response = requests.request("POST", url, headers=get_header_data(), data=json.dumps(get_payload_data_for_item(self , publish)))
        if response.status_code == 200:
            frappe.msgprint(f'Item {self.name} is Created Successfully in ASP.' , alert=True , indicator='green')
            self.custom_inserted_to_asp = 1 
        else: 
            frappe.throw(f" Create Item : {str(response.text)}")

def update_item_in_asp(self , publish):
    if publish:
        url = f"{get_base_url()}UGCEditProduct.ashx"
        response = requests.request("POST", url, headers=get_header_data(), data=json.dumps(get_payload_data_for_item(self , publish)))
        if response.status_code == 200:
            frappe.msgprint(f'Item {self.name} is updated Successfully in ASP.' , alert=True , indicator='green')
        else: 
            frappe.throw(f" Update Item : {str(response.text)}")