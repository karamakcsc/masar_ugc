


import frappe
from frappe.model.naming import make_autoname
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