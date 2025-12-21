app_name = "masar_ugc"
app_title = "Masar UGC"
app_publisher = "KCSC"
app_description = "Masar UGC"
app_email = "info@kcsc.com.jo"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/masar_ugc/css/masar_ugc.css"
# app_include_js = "/assets/masar_ugc/js/masar_ugc.js"

# include js, css files in header of web template
# web_include_css = "/assets/masar_ugc/css/masar_ugc.css"
# web_include_js = "/assets/masar_ugc/js/masar_ugc.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "masar_ugc/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "masar_ugc/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "masar_ugc.utils.jinja_methods",
# 	"filters": "masar_ugc.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "masar_ugc.install.before_install"
# after_install = "masar_ugc.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "masar_ugc.uninstall.before_uninstall"
# after_uninstall = "masar_ugc.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "masar_ugc.utils.before_app_install"
# after_app_install = "masar_ugc.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "masar_ugc.utils.before_app_uninstall"
# after_app_uninstall = "masar_ugc.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "masar_ugc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"validate": "masar_ugc.custom.item.item.validate"
	}, 
    "Quotation": {
        "on_submit" : "masar_ugc.custom.quotation.quotation.on_submit", 
        "autoname" : "masar_ugc.custom.quotation.quotation.autoname"
    }
}
doctype_js = {
#    "Customer" : "custom/customer/customer.js"
    "Employee": "custom/employee/employee.js",
    "Quotation" : "custom/quotation/quotation.js"
    # "Item": "custom/item/item.js"
 }
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"masar_ugc.tasks.all"
# 	],
# 	"daily": [
# 		"masar_ugc.tasks.daily"
# 	],
# 	"hourly": [
# 		"masar_ugc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"masar_ugc.tasks.weekly"
# 	],
# 	"monthly": [
# 		"masar_ugc.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "masar_ugc.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "masar_ugc.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "masar_ugc.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["masar_ugc.utils.before_request"]
# after_request = ["masar_ugc.utils.after_request"]

# Job Events
# ----------
# before_job = ["masar_ugc.utils.before_job"]
# after_job = ["masar_ugc.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"masar_ugc.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Item-custom_more_details",
                "Item-custom_masar_id",
                "Item-custom_visible",
                "Item-custom_column_break_2hsra",
                "Item-custom_sold",
                "Item-custom_section_break_k9luu",
                "Item-custom_category_en",
                "Item-custom_column_break_fus0k",
                "Item-custom_category_ar",
                "Item-custom_column_break_k78p3",
                "Item-custom_category_fr",
                "Item-custom_brand_en",
                "Item-custom_brand_ar",
                "Item-custom_brand_fr",
                "Item-custom_subbrand1_en",
                "Item-custom_subbrand1_ar",
                "Item-custom_subbrand1_fr",
                "Item-custom_product_name_en",
                "Item-custom_product_name_ar",
                "Item-custom_product_name_fr",
                "Item-custom_short_disc_en",
                "Item-custom_short_disc_ar",
                "Item-custom_short_disc_fr",
                "Item-custom_product_use_en",
                "Item-custom_product_use_ar",
                "Item-custom_product_use_fr",
                "Item-custom_surface1_en",
                "Item-custom_surface2_en",
                "Item-custom_surface3_en",
                "Item-custom_surface1_ar",
                "Item-custom_surface2_ar",
                "Item-custom_surface3_ar",
                "Item-custom_surface1_fr",
                "Item-custom_surface2_fr",
                "Item-custom_surface3_fr",
                "Item-custom_finishes_en",
                "Item-custom_finishes_ar",
                "Item-custom_finishes_fr",
                "Item-custom_colors_en",
                "Item-custom_colors_ar",
                "Item-custom_colors_fr",
                "Item-custom_sheen_en",
                "Item-custom_sheen_ar",
                "Item-custom_sheen_fr",
                "Item-custom_packsize_en",
                "Item-custom_packsize_ar",
                "Item-custom_packsize_fr",
                "Item-custom_coverageperpack_en",
                "Item-custom_applicationtool_en",
                "Item-custom_coverageperpack_ar",
                "Item-custom_applicationtool_ar",
                "Item-custom_coverageperpack_fr",
                "Item-custom_applicationtool_fr",
                "Item-custom_links",
                "Item-custom_subbrand_pic_en",
                "Item-custom_column_break_k37i5",
                "Item-custom_subbrand_pic_ar",
                "Item-custom_column_break_aj825",
                "Item-custom_subbrand_pic_fr",
                "Item-custom_subbrand_ved_en",
                "Item-custom_tds_en",
                "Item-custom_msds_en",
                "Item-custom_subbrand_ved_ar",
                "Item-custom_tds_ar",
                "Item-custom_msds_ar",
                "Item-custom_subbrand_ved_fr",
                "Item-custom_tds_fr",
                "Item-custom_msds_fr",
                "Item-custom_meta",
                "Item-custom_metadisc_en",
                "Item-custom_column_break_fjuwk",
                "Item-custom_metadisc_ar",
                "Item-custom_column_break_qnpzb",
                "Item-custom_metadisc_fr",
                "Item-custom_section_break_slnq0",
                "Item-custom_long_disc_en",
                "Item-custom_column_break_6xuw8",
                "Item-custom_long_disc_ar",
                "Item-custom_column_break_xmeo3",
                "Item-custom_long_disc_fr",
                "Item-custom_long_desc_ar",
                "Item-custom_long_desc_fr",
                "Item-custom_short_desc",
                "Item-custom_column_break_nemtx",
                "Item-custom_column_break_h4rgs",
                "Item-custom_product_details",
                "Item-custom_column_break_ayb4e",
                "Item-custom_column_break_hlizb",
                "Item-custom_color_details",
                "Item-custom_column_break_bchap",
                "Item-custom_column_break_nngsj",
                "Brand-custom_is_enabled",
                "Brand-custom_brand_fr",
                "Brand-custom_brand_ar",
                "Quotation-custom_left_header",
                "Quotation-custom_project",
                "Incoterm-custom_section_break_4t80x",
                "Incoterm-custom_is_enable",
                "Incoterm-custom_column_break_dgsft",
                "Quotation-custom_incoterms",
                "Quotation-custom_quotation_type",
                "Quotation-custom_left_header_link",
                "Quotation-custom_column_break_tqgal",
                "Quotation-custom_right_header_link",
                "Quotation-custom_right_header",
                "Tax Category-custom_column_break_fy4ai", 
                "Tax Category-custom_sales_taxes_and_charges_template",
                "Brand-custom_column_break_jkogk",
                "Brand-custom_section_break_u71wi",
                "Brand-custom_brand_name_fr",
                "Brand-custom_brand_name_ar", 
                "Item-custom_subbrand2_en", 
                "Item-custom_subbrand2_ar", 
                "Item-custom_subbrand2_fr", 
                "Item-custom_applicationtool_2_en" , 
                "Item-custom_applicationtool_2_ar" , 
                "Item-custom_applicationtool_2_fr" , 
                "Item-custom_applicationtool_3_en" , 
                "Item-custom_applicationtool_3_ar" , 
                "Item-custom_applicationtool_3_fr" , 
                "Quotation Item-custom_section_break_lf7wl" , 
                "Quotation Item-custom_color" , 
                "Quotation Item-custom_pack_size" , 
                "Quotation Item-custom_column_break_im5er" , 
                "Quotation Item-custom_no_of_coats" , 
                "Quotation Item-custom_spr_rate",
                "Quotation Item-custom_dft_no_of_coats",
                "Quotation-custom_attention",
                "Item-custom_is_publish",
                "Quotation-custom_payment_term",
                "Quotation-custom_address",
                "Quotation-custom_title1", 
                "Quotation-custom_section_break_nvp9m", 
                "Quotation-custom_title2", 
                "Quotation-custom_items2", 
                "Quotation-custom_section_break_qvuqs", 
                "Quotation-custom_title3",
                "Quotation-custom_items3",
                "Quotation-custom_coats_or_dft", 
                "Item-custom_friendly_url",
                "Item-custom_inserted_to_asp",
                "Project Type-custom_posting_date",
                "Project Type-custom_column_break_brwiu",
                "Project Type-custom_enabled",
                "Project Type-custom_section_break_ldxao",
                "Quotation-custom_project_type",
                "Item-custom_practical_spreading_rate_en",
                "Item-custom_practical_spreading_rate_ar",
                "Item-custom_practical_spreading_rate_fr",
                "Item-custom_section_break_6fgby",
                "Item-custom_keyfeatures_en",
                "Item-custom_column_break_fgjyr",
                "Item-custom_keyfeatures_ar",
                "Item-custom_column_break_pgxlq",
                "Item-custom_keyfeatures_fr" , 
                "Item-custom_filter_data" , 
                "Item-custom_section_break_ogopp",
                "Quotation-custom_titles",
                "Item-custom_item_name_ar" , 
                "Item-custom_solid_content" , 
                "Item-custom_spreading_rate" , 
                "Item-custom_dft_desc" , 
                "Item-custom_dft" , 
                "Quotation Item-custom_dft",
                "Quotation-custom_column_break_wgdmx",
                "Quotation Item-custom_column_break_ys4g4",
                "Quotation-custom_column_break_aqejd",
                "Item-custom_solid_content",
                "Quotation Item-custom_system_entry",
                "Item-custom_system_entry",
                "Item-custom_is_system",
                "Item-custom_short_disc_fr_2",
                "Item-custom_short_disc_ar_2",
                "Item-custom_short_disc_en_2",
                "Item-custom_metadisc_fr_2",
                "Item-custom_metadisc_ar_2",
                "Item-custom_metadisc_en_2",
                "Item-custom_no_of_coats",
                "Item-custom_is_hero"
            ]
        ]
    ]},
     {
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                    "Quotation-main-field_order",
                    # "Quotation-payment_schedule_section-hidden",
                    "Quotation-pricing_rule_details-hidden",
                    "Quotation-bundle_items_section-hidden",
                    "Quotation-sec_tax_breakup-hidden",
                    "Quotation-section_break_44-hidden",
                    "Quotation-totals-hidden",
                    "Quotation-items-allow_bulk_edit",
                    "Quotation-named_place-hidden",
                    "Quotation-incoterm-hidden",
                    "Quotation-shipping_rule-hidden",
                    "Quotation-net_total-hidden",
                    "Quotation-total-hidden",
                    "Quotation-total_net_weight-hidden",
                    "Quotation-total_qty-hidden",
                    "Quotation-scan_barcode-hidden",
                    "Quotation-more_info_tab-hidden",
                    "Quotation-order_type-hidden",
                    "Quotation-in_words-print_hide",
                    "Quotation-in_words-hidden",
                    "Quotation-disable_rounded_total-default",
                    "Quotation-rounded_total-print_hide",
                    "Quotation-rounded_total-hidden",
                    "Quotation-base_rounded_total-print_hide",
                    "Quotation-base_rounded_total-hidden",
                    "Quotation-taxes_and_charges-fetch_from",
                    "Quotation-sec_break23-hidden", 
                    "Quotation-base_total_taxes_and_charges-hidden" , 
                    "Quotation-total_taxes_and_charges-hidden",
                    "Quotation-quotation_to-hidden",
                    "Quotation Item-item_name-in_list_view",
                    "Quotation-company-default",
                    "Quotation-address_and_contact_tab-hidden",
                    "Quotation-main-field_order",
                    "Quotation-party_name-in_standard_filter",
                    "Quotation-payment_terms_template-reqd",
                    "Quotation-order_type-in_standard_filter",
                    "Item-main-field_order",
                    "Quotation Item-main-field_order",
                    "Quotation-customer_address-hidden",
                    "Quotation-main-field_order",
                    "Quotation Item-gross_profit-hidden",
                    "Quotation Item-valuation_rate-hidden",
                    "Quotation Item-section_break_43-hidden",
                    "Quotation Item-is_alternative-hidden",
                    "Quotation Item-is_free_item-hidden",
                    "Quotation Item-uom-in_list_view",
                    "Quotation Item-item_code-columns",
                    "Quotation Item-qty-columns",
                    "Quotation Item-uom-columns"
                ]
            ]
        ]
    }
]