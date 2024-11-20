import frappe 
from datetime import date

@frappe.whitelist()
def get_employee_details():
    user = 'masterpainter@ugc.jo'#frappe.session.user#
    e = frappe.qb.DocType('Employee')
    sql = (frappe.qb.from_(e).select(
        (e.first_name) , (e.middle_name) , (e.last_name) , (e.department) , (e.image)
        )
        .where(e.user_id == user
        )
    ).run(as_dict = True)
    if len(sql) != 0 : 
        return {
            'first_name' : sql[0]['first_name'],
            'middle_name' : sql[0]['middle_name'],
            'last_name' : sql[0]['last_name'],
            'department' : sql[0]['department'],
            'image' : sql[0]['image']
        }
    else:
        return False  
        
@frappe.whitelist()
def get_announcement():
    today = date.today()
    a = frappe.qb.DocType('Announcement')
    sql = (
        frappe.qb.from_(a)
        .select((a.title) , (a.announcement) )
        .where(a.from_date <= today)
        .where(a.to_date >= today)
        
    ).run(as_dict = True)
    return sql 

@frappe.whitelist()
def get_item_details():
    return frappe.db.sql("""
                         SELECT 
                            item_code ,item_name, custom_visible ,custom_sold ,custom_category_en ,
                            custom_category_ar ,custom_category_fr ,custom_brand_en ,custom_brand_ar ,custom_brand_fr ,custom_subbrand1_en ,
                            custom_subbrand1_ar ,custom_subbrand1_fr ,custom_subbrand2_en , custom_subbrand2_ar , custom_subbrand2_fr , 
                            custom_product_name_en , custom_product_name_ar , custom_product_name_fr , custom_short_disc_en ,
                            custom_short_disc_ar ,custom_short_disc_fr ,custom_product_use_en ,custom_product_use_ar ,custom_product_use_fr ,custom_surface1_en ,custom_surface2_en ,
                            custom_surface3_en ,custom_surface1_ar , custom_surface2_ar ,custom_surface3_ar ,custom_surface1_fr ,custom_surface2_fr ,custom_surface3_fr ,custom_finishes_en , custom_finishes_ar ,custom_finishes_fr ,
                            custom_colors_en ,custom_colors_ar ,custom_colors_fr ,custom_sheen_en ,custom_sheen_ar ,custom_sheen_fr ,
                            custom_packsize_en ,custom_packsize_ar ,custom_packsize_fr ,custom_coverageperpack_en ,custom_applicationtool_en ,custom_coverageperpack_ar ,custom_applicationtool_ar ,
                            custom_coverageperpack_fr , custom_applicationtool_fr , custom_subbrand_pic_en ,custom_subbrand_pic_ar ,
                            custom_subbrand_pic_fr ,custom_subbrand_ved_en , custom_tds_en ,custom_msds_en ,custom_subbrand_ved_ar ,
                            custom_tds_ar ,custom_msds_ar ,custom_subbrand_ved_fr ,custom_tds_fr ,custom_msds_fr ,custom_metadisc_en ,
                            custom_metadisc_ar ,custom_metadisc_fr , custom_long_disc_en ,custom_long_disc_ar ,custom_long_disc_fr ,
                            custom_applicationtool_2_en , custom_applicationtool_2_ar , custom_applicationtool_2_fr, custom_applicationtool_3_en , 
                            custom_applicationtool_3_ar , custom_applicationtool_3_fr
                        FROM tabItem ti """)
    