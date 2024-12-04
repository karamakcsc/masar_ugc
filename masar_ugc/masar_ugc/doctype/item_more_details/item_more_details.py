# Copyright (c) 2024, KCSC and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class ItemMoreDetails(Document):
#     def on_submit(self):
#         self.update_item_details()
        
#     def update_item_details(self):
#         item_doc = frappe.get_doc("Item", self.item)
#         data = {
#                 'custom_visible' : self.upd_visible , 
#                 'custom_sold' : self.upd_sold,
#                 'custom_category_en' : self.upd_category_en,
#                 'custom_brand_en' : self.upd_brand_en,
#                 'custom_subbrand1_en' : self.upd_subbrand1_en,
#                 'custom_subbrand2_en' : self.upd_subbrand2_en,
#                 'custom_product_name_en' : self.upd_product_name_en,
#                 'custom_product_name_ar' : self.upd_product_name_ar,
#                 'custom_product_name_fr' : self.upd_product_name_fr,
#                 'custom_product_use_en' : self.upd_product_use_en,
#                 'custom_surface1_en' : self.upd_surface1_en,
#                 'custom_surface2_en' : self.upd_surface2_en,
#                 'custom_surface3_en' : self.upd_surface3_en,
#                 'custom_finishes_en' : self.upd_finishes_en,
#                 'custom_colors_en' : self.upd_colors_en,
#                 'custom_colors_ar' : self.upd_colors_ar,
#                 'custom_colors_fr' : self.upd_colors_fr,
#                 'custom_sheen_en' : self.upd_sheen_en
#             }
#         item_doc.update(data)
#         item_doc.save()
#         frappe.msgprint(f'Item: {self.item} Updated Successfully.' , alert=True, indicator='green')
#     pass
