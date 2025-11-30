import frappe
import json
from frappe.model.naming import make_autoname
from frappe.utils import flt, ceil


def on_submit(self , method): 
    headers_validate(self)

def headers_validate(self): 
    h = frappe.qb.DocType("Header")
    if self.custom_left_header_link is None and self.custom_left_header is None: 
        
        exist = (
        			frappe.qb.from_(h)
           				.select(h.name)
               			.where(h.defualt ==1 )
						.where(h.is_enable ==1 )
						.where(h.left_header ==1 )
                ).run()
        if not (exist and exist[0] and exist[0][0]):
            frappe.throw('Left Header must be Selected or Set Defualt Left Header.')
    if self.custom_right_header_link is None and self.custom_right_header is None: 
        q = frappe.qb.DocType('Quotation')
        exist = (
        			frappe.qb.from_(h)
           				.select(h.name)
               			.where(h.defualt ==1 )
						.where(h.is_enable ==1 )
						.where(h.right_header ==1 )
                ).run()
        if not (exist and exist[0] and exist[0][0]):
            frappe.throw('Right Header must be Selected or Set Defualt Left Header.')

def autoname(self , method): 
    h = frappe.qb.DocType('Header')
    user = frappe.session.user
    e = frappe.qb.DocType('Employee')
    sql = frappe.frappe.qb.from_(e).select(e.first_name , e.last_name).where(e.user_id == user).run(as_dict = True)
    if sql and sql[0]:
        full_name = sql[0]
        if full_name['first_name']:
            f_name = full_name['first_name'].split()
            first_initial = f_name[0][0]
        else: 
            first_initial = 'N-A'
        if full_name['last_name']:
            l_name = full_name['last_name'].split()
            last_initial = l_name[0][0]
        else: 
            last_initial = 'N-A'
    else: 
            first_initial = 'FN-A'
            last_initial = 'LN-A'
    part_one = str(first_initial + last_initial)
    part_two = "SO"
    headers_validate(self)
    if self.custom_left_header_link:
        doc = frappe.get_doc('Header' , self.custom_left_header_link)
        abbr = doc.abbr
    else: 
        abbr = (
        			frappe.qb.from_(h)
           				.select(h.abbr)
               			.where(h.defualt ==1)
						.where(h.is_enable ==1)
						.where(h.left_header ==1)
                ).run()
    part_three = abbr[0][0]
    part_four =".######"
    self.name = make_autoname(f"{part_one}/{part_two}/{part_three}/{part_four}")
    
@frappe.whitelist()
def set_tax(self):
    if isinstance(self, str):
        self = json.loads(self)
    
    if isinstance(self, dict):
        self = frappe._dict(self)
    
    if not self.get("items") or not self.get("tax_category"):
        return

    quotation_doc = frappe.get_doc("Quotation", self.get("name"))
    
    tax_percent = 0 if self.get("tax_category") == "0%" else 16
    
    for item in quotation_doc.items:

        if not item.get("original_rate"):
            item.original_rate = item.rate

        base_rate = item.original_rate 

        if tax_percent == 0:
            item.rate = round(base_rate / 1.16, 3)

        else:
            item.rate = base_rate

    build_taxes_table(quotation_doc, tax_percent)
    quotation_doc.save()
    
    return quotation_doc.as_dict()

def build_taxes_table(doc, tax_percent):
    doc.set("taxes", [])

    if tax_percent == 0:
        return

    total = sum([item.rate * item.qty for item in doc.items])
    total_tax = round(total * (tax_percent / 100), 3)

    doc.append("taxes", {
        "charge_type": "On Net Total",
        "account_head": "VAT - UGCD",
        "description": f"Sales Tax {tax_percent}%",
        "rate": tax_percent,
        "tax_amount": total_tax
    })

@frappe.whitelist()    
def fetch_system_items(system_name, sys_qty):
    system_entry = frappe.get_doc("System Entry", system_name)
    items = []
    for system_item in system_entry.proposed_systems:
        item = frappe.get_doc("Item", system_item.item_code)
        qty = flt(sys_qty)/flt(item.custom_spreading_rate) if item.custom_spreading_rate and item.custom_spreading_rate > 0 else 1 
        items.append({
            "item_code": system_item.item_code,
            "item_name": system_item.item_name,
            "description": item.description,
            "qty": ceil(qty),
            "uom": item.stock_uom,
        })
    return items