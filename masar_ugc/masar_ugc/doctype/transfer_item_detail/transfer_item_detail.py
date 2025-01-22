# Copyright (c) 2025, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TransferItemDetail(Document):
    def on_submit(self):
        self.transfer_details()
    
    
    def transfer_details(self):
        item_details_sql = frappe.db.sql("""
                          SELECT 
                                ti.custom_category_en , ti.custom_category_ar ,ti.custom_category_fr ,ti.custom_brand_en ,ti.custom_brand_ar ,ti.custom_brand_fr ,ti.custom_subbrand1_en ,
                                ti.custom_subbrand1_ar ,ti.custom_subbrand1_fr ,ti.custom_subbrand2_en , ti.custom_subbrand2_ar , ti.custom_subbrand2_fr , 
                                ti.custom_short_disc_en , ti.custom_short_disc_ar ,ti.custom_short_disc_fr ,ti.custom_product_use_en ,ti.custom_product_use_ar ,ti.custom_product_use_fr ,ti.custom_surface1_en ,ti.custom_surface2_en ,
                                ti.custom_surface3_en ,ti.custom_surface1_ar , ti.custom_surface2_ar ,ti.custom_surface3_ar ,ti.custom_surface1_fr ,ti.custom_surface2_fr ,ti.custom_surface3_fr ,ti.custom_finishes_en , ti.custom_finishes_ar ,ti.custom_finishes_fr ,
                                ti.custom_colors_en ,ti.custom_colors_ar ,ti.custom_colors_fr ,ti.custom_sheen_en ,ti.custom_sheen_ar ,ti.custom_sheen_fr ,
                                ti.custom_packsize_en ,ti.custom_packsize_ar ,ti.custom_packsize_fr ,ti.custom_coverageperpack_en ,ti.custom_applicationtool_en ,ti.custom_coverageperpack_ar ,ti.custom_applicationtool_ar ,
                                ti.custom_coverageperpack_fr , ti.custom_applicationtool_fr , ti.custom_subbrand_pic_en ,ti.custom_subbrand_pic_ar ,
                                ti.custom_subbrand_pic_fr ,ti.custom_subbrand_ved_en , ti.custom_tds_en ,ti.custom_msds_en ,ti.custom_subbrand_ved_ar ,
                                ti.custom_tds_ar ,ti.custom_msds_ar ,ti.custom_subbrand_ved_fr ,ti.custom_tds_fr ,ti.custom_msds_fr ,ti.custom_metadisc_en ,
                                ti.custom_metadisc_ar ,ti.custom_metadisc_fr , ti.custom_long_disc_en ,ti.custom_long_disc_ar ,ti.custom_long_disc_fr ,    ti.custom_applicationtool_2_en , ti.custom_applicationtool_2_ar , ti.custom_applicationtool_2_fr, ti.custom_applicationtool_3_en , 
                                ti.custom_applicationtool_3_ar , ti.custom_applicationtool_3_fr , ti.custom_friendly_url, ti.image 
                            FROM tabItem ti
                            WHERE  ti.name = %s
                        """,(self.source_item,), as_dict= True)
        if item_details_sql and item_details_sql[0]:
            for item in self.items:
                doc = frappe.get_doc("Item", item.item_code).update(item_details_sql[0]).save()
            
                
