import frappe 
from datetime import date

@frappe.whitelist()
def get_employee_details():
    '''
    HTML: 
                <h4>Employee Details</h4><br><br><br>
            <div id="employee-info" style="display: flex; align-items: center; width: 100%; height: 30px;">
                
                <img id="employee-image" class="qr-code" src="" style="height: 4cm; width: 6cm; flex: 1;" alt="Employee Image">
                <div class="print-heading" style="flex: 2;width: 10%; text-align: left;"></div>
                <div class="print-heading" style="flex: 3; text-align: left;">
                    <div id="employee_name"></div>
                    <div id="cell_number"></div>
                    <div id="department"></div>
                </div>
            </div><br><br><br><br><br><br>
            
    JS: 
    
        frappe.call({
                method: "masar_ugc.api.get_employee_details",
                callback(r) {
                    if (r.message) {
                        root_element.querySelector("#employee_name").innerHTML = '<b>First Name:</b><br>' + (r.message.employee_name || '');
                        root_element.querySelector("#cell_number").innerHTML = '<b>Mobile:</b><br>' + (r.message.cell_number || '');
                        root_element.querySelector("#department").innerHTML = '<b>Department:</b><br>' + (r.message.department || '');
                        root_element.querySelector('#employee-image').src = r.message.image || '';
                    } else {
                        console.error("Employee not found for the specified ID.");
                    }
                },
                error(err) {
                    console.error("Error fetching employee data:", err);
                }
            });
    '''
    user = frappe.session.user#'masterpainter@ugc.jo'#
    e = frappe.qb.DocType('Employee')
    sql = (frappe.qb.from_(e).select(
        (e.employee_name) , (e.cell_number) , (e.department) , (e.image)
        )
        .where(e.user_id == user
        )
    ).run(as_dict = True)
    if len(sql) != 0 : 
        return {
            'employee_name' : sql[0]['employee_name'],
            'cell_number' : sql[0]['cell_number'],
            'department' : sql[0]['department'],
            'image' : sql[0]['image']
        }
    else:
        return False  
        
@frappe.whitelist()
def get_announcement():
    """
    HTML: 
            <h4>Announcements</h4>
            <div id="title"></div>
            <div id="announcement"></div>
            
    JS: 
    
        frappe.call({
        method: "masar_ugc.api.get_announcement",
        callback(r) {
            if (r.message && Array.isArray(r.message)) {
                let announcements = r.message; 
                let index = 0;
                const allAnnouncements = announcements.map(announcement => {
                    return `<b>Title:</b> ${announcement.title || ''}<br><b>Details:</b> ${announcement.announcement || ''}<br><br>`;
                }).join('');

                function displayAnnouncement() {
                    const announcement = announcements[index];
                    root_element.querySelector("#title").innerHTML = '<b>Title:</b> ' + (announcement.title || '');
                    root_element.querySelector("#announcement").innerHTML = '<br><b>Details</b><br>' + (announcement.announcement || '');
                    index++;
                    if (index >= announcements.length) {
                        index = 0;
                    }
                }
                displayAnnouncement();
                const intervalId = setInterval(displayAnnouncement, 25000);

                // Add click event listener to the root element
                root_element.addEventListener('click', () => {
                    frappe.msgprint(allAnnouncements , title= frappe._("Announcements"));
                });
            } else {
                console.error("No announcements found.");
            }
        },
        error(err) {
            console.error("Error fetching announcements:", err);
        }
    });"""
    if frappe.session.user == 'Administrator':
        today = date.today()
        a = frappe.qb.DocType('Announcement')
        sql = (
            frappe.qb.from_(a)
            .select((a.title) , (a.announcement) )
            .where(a.from_date <= today)
            .where(a.to_date >= today)
            
        ).run(as_dict = True)
        return sql 
    user = frappe.session.user
    today = date.today()
    a = frappe.qb.DocType('Announcement')
    ugm = frappe.qb.DocType('User Group Member')
    sql = (
        frappe.qb.from_(a)
        .join(ugm).on(ugm.parent == a.name)
        .select((a.title) , (a.announcement) , (ugm.user))
        .where(a.from_date <= today)
        .where(a.to_date >= today)
    ).run(as_dict = True)
    data = list()
    for s in sql: 
        if user == s.user:
            data.append(s)
      
    return data 
    
    
@frappe.whitelist()
def get_item_details():
    return frappe.db.sql("""
                SELECT 
                    ti.item_code, ti.item_name,  ti.custom_visible,  ti.custom_sold,  ti.custom_category_en, ti.custom_category_ar, ti.custom_category_fr, 
                    ti.custom_brand_en, ti.custom_brand_ar,  ti.custom_brand_fr,  ti.custom_subbrand1_en, ti.custom_subbrand1_ar, ti.custom_subbrand1_fr, 
                    ti.custom_subbrand2_en, ti.custom_subbrand2_ar, ti.custom_subbrand2_fr, ti.custom_short_disc_en, ti.custom_short_disc_ar, 
                    ti.custom_short_disc_fr, ti.custom_product_use_en, ti.custom_product_use_ar, ti.custom_product_use_fr, ti.custom_surface1_en, 
                    ti.custom_surface2_en, ti.custom_surface3_en, ti.custom_surface1_ar, ti.custom_surface2_ar, ti.custom_surface3_ar, 
                    ti.custom_surface1_fr, ti.custom_surface2_fr, ti.custom_surface3_fr, ti.custom_finishes_en, ti.custom_finishes_ar, 
                    ti.custom_finishes_fr, ti.custom_colors_en, ti.custom_colors_ar, ti.custom_colors_fr, ti.custom_sheen_en, ti.custom_sheen_ar, 
                    ti.custom_sheen_fr, ti.custom_packsize_en, ti.custom_packsize_ar, ti.custom_packsize_fr, ti.custom_coverageperpack_en, 
                    ti.custom_applicationtool_en, ti.custom_coverageperpack_ar,  ti.custom_applicationtool_ar, ti.custom_coverageperpack_fr, ti.custom_applicationtool_fr, 
                    ti.custom_subbrand_pic_en, ti.custom_subbrand_pic_ar, ti.custom_subbrand_pic_fr, ti.custom_subbrand_ved_en, ti.custom_tds_en, ti.custom_msds_en, 
                    ti.custom_subbrand_ved_ar,  ti.custom_tds_ar, ti.custom_msds_ar, ti.custom_subbrand_ved_fr,  ti.custom_tds_fr, ti.custom_msds_fr, 
                    ti.custom_metadisc_en, ti.custom_metadisc_ar, ti.custom_metadisc_fr, ti.custom_long_disc_en, ti.custom_long_disc_ar, 
                    ti.custom_long_disc_fr,  ti.custom_applicationtool_2_en, ti.custom_applicationtool_2_ar,  ti.custom_applicationtool_2_fr,  ti.custom_applicationtool_3_en, 
                    ti.custom_applicationtool_3_ar, ti.custom_applicationtool_3_fr,  ti.custom_friendly_url, 
                    COALESCE(
                        CASE 
                            WHEN ti.image IS NULL OR TRIM(ti.image) = '' THEN NULL
                            ELSE CONCAT('https://ugc.kcsc.com.jo', ti.image)
                        END,
                        CONCAT('https://ugc.kcsc.com.jo', tdi.default_image)
                    ) AS image_url
                FROM tabItem ti
                LEFT JOIN `tabDefault Image` tdi ON ti.custom_brand_en = tdi.brand AND tdi.is_product = 1 
                WHERE disabled = 0 AND custom_visible = 1 AND workflow_state = 'Publish' """, as_dict= True)



@frappe.whitelist()
def get_category_details():
    return frappe.db.sql("""
                         SELECT 
                            category_name, category_name_ar, category_name_fr, category_meta_disc_en,
                            category_meta_disc_ar, category_meta_disc_fr
                        FROM tabCategory tc
                        WHERE is_enabled = 1 """, as_dict= True)

@frappe.whitelist()
def get_surface_details():
    return frappe.db.sql("""
                         SELECT 
                            surface1_en, surface1_ar, surface1_fr,
                            surfacemetadiscen, surfacemetadiscar, surfacemetadiscfr 
                        FROM tabSurface ts
                        WHERE is_enabled = 1 """, as_dict= True)


@frappe.whitelist()
def get_system_master():
    systems = frappe.db.sql("""
        SELECT 
            tpse.name, tpse.system_no, 
            tpse.area_of_use_en, tpse.area_of_use_ar, tpse.area_of_use_fr, 
            tpse.area_of_use_en_2, tpse.area_of_use_ar_2, tpse.area_of_use_fr_2, 
            tpse.area_of_use_en_3, tpse.area_of_use_ar_3, tpse.area_of_use_fr_3, 
            tpse.area_of_use_metadiscen, tpse.area_of_use_metadiscar, tpse.area_of_use_metadiscfr, 
            tpse.sub_area_of_use_en, tpse.sub_area_of_use_ar, tpse.sub_area_of_use_fr, 
            tpse.system_brand, 
            tpse.system_name_en, tpse.system_name_ar, tpse.system_name_fr, 
            tpse.system_image_link, tpse.system_video_link, tpse.test_result_link, tpse.statement_link, 
            tpse.system_metadisc_en, tpse.system_metadisc_ar, tpse.system_metadisc_fr,
            tpse.system_description_en, tpse.system_description_ar, tpse.system_description_fr, 
            COALESCE(
		        CASE 
		            WHEN tpse.image IS NULL OR TRIM(tpse.image) = '' THEN NULL
		            ELSE CONCAT('https://ugc.kcsc.com.jo', tpse.image)
		        END,
		        CONCAT('https://ugc.kcsc.com.jo', tdi.default_image)
		    ) AS image_url,
		    COALESCE(
		        CASE 
		            WHEN tpse.body_image IS NULL OR TRIM(tpse.body_image) = '' THEN NULL
		            ELSE CONCAT('https://ugc.kcsc.com.jo', tpse.body_image)
		        END,
		        CONCAT('https://ugc.kcsc.com.jo', tdi.default_image)
		    ) AS body_image
        FROM `tabSystem Entry` tpse
        LEFT JOIN `tabDefault Image` tdi ON tpse.system_brand = tdi.brand AND tdi.is_system =1 
        WHERE tpse.is_published = 1 AND tpse.workflow_state = 'Publish'
    """, as_dict=True)

    for system in systems:
        children = frappe.db.sql("""
            SELECT 
                tpsi.name, tpsi.idx,tpsi.product_use_en, tpsi.product_use_ar, tpsi.product_use_fr, tpsi.no_coat_en, tpsi.no_coat_ar, tpsi.no_coat_fr, tpsi.item_code, 
                ti.custom_subbrand2_en, ti.custom_subbrand2_ar, ti.custom_subbrand2_fr
            FROM `tabProposed System Item` tpsi
            INNER JOIN `tabItem` ti ON tpsi.item_code = ti.name
            WHERE tpsi.parent = %s
        """, (system['name'],), as_dict=True)
        system['proposed_system_items'] = children

    return systems


@frappe.whitelist()
def get_item(item_code = None):
    cond = None
    if item_code:
        cond = f""" AND item_code = '{item_code}'"""
    return frappe.db.sql(f"""
                          SELECT 
                                ti.item_code ,ti.item_name, ti.custom_visible ,ti.custom_sold ,ti.custom_category_en ,
                                ti.custom_category_ar ,ti.custom_category_fr ,ti.custom_brand_en ,ti.custom_brand_ar ,ti.custom_brand_fr ,ti.custom_subbrand1_en ,
                                ti.custom_subbrand1_ar ,ti.custom_subbrand1_fr ,ti.custom_subbrand2_en , ti.custom_subbrand2_ar , ti.custom_subbrand2_fr , 
                                ti.custom_short_disc_en ,
                                ti.custom_short_disc_ar ,ti.custom_short_disc_fr ,ti.custom_product_use_en ,ti.custom_product_use_ar ,ti.custom_product_use_fr ,ti.custom_surface1_en ,ti.custom_surface2_en ,
                                ti.custom_surface3_en ,ti.custom_surface1_ar , ti.custom_surface2_ar ,ti.custom_surface3_ar ,ti.custom_surface1_fr ,ti.custom_surface2_fr ,ti.custom_surface3_fr ,ti.custom_finishes_en , ti.custom_finishes_ar ,ti.custom_finishes_fr ,
                                ti.custom_colors_en ,ti.custom_colors_ar ,ti.custom_colors_fr ,ti.custom_sheen_en ,ti.custom_sheen_ar ,ti.custom_sheen_fr ,
                                ti.custom_packsize_en ,ti.custom_packsize_ar ,ti.custom_packsize_fr ,ti.custom_coverageperpack_en ,ti.custom_applicationtool_en ,ti.custom_coverageperpack_ar ,ti.custom_applicationtool_ar ,
                                ti.custom_coverageperpack_fr , ti.custom_applicationtool_fr , ti.custom_subbrand_pic_en ,ti.custom_subbrand_pic_ar ,
                                ti.custom_subbrand_pic_fr ,ti.custom_subbrand_ved_en , ti.custom_tds_en ,ti.custom_msds_en ,ti.custom_subbrand_ved_ar ,
                                ti.custom_tds_ar ,ti.custom_msds_ar ,ti.custom_subbrand_ved_fr ,ti.custom_tds_fr ,ti.custom_msds_fr ,ti.custom_metadisc_en ,
                                ti.custom_metadisc_ar ,ti.custom_metadisc_fr , ti.custom_long_disc_en ,ti.custom_long_disc_ar ,ti.custom_long_disc_fr ,    ti.custom_applicationtool_2_en , ti.custom_applicationtool_2_ar , ti.custom_applicationtool_2_fr, ti.custom_applicationtool_3_en , 
                                ti.custom_applicationtool_3_ar , ti.custom_applicationtool_3_fr , ti.custom_friendly_url,  
                            COALESCE(
                                                    CASE 
                                                        WHEN ti.image IS NULL OR TRIM(ti.image) = '' THEN NULL
                                                        ELSE CONCAT('https://ugc.kcsc.com.jo', ti.image)
                                                    END,
                                                    CONCAT('https://ugc.kcsc.com.jo', tdi.default_image)
                                                ) AS image_url
                                            FROM tabItem ti
                                            LEFT JOIN `tabDefault Image` tdi ON ti.custom_brand_en = tdi.brand AND tdi.is_product = 1 
                            WHERE  disabled = 0 
                            AND custom_visible = 1 
                            AND workflow_state = 'Publish' 
                        {cond}""", as_dict= True)



@frappe.whitelist()
def get_area_of_use():
    return frappe.db.sql("""
                         SELECT 
                            area_of_use_en, area_of_use_ar, area_of_use_fr,
                            area_of_use_metadiscen, area_of_use_metadiscar, area_of_use_metadiscfr
                        FROM `tabArea of Use`
                        WHERE is_enabled = 1 """, as_dict= True)
    


def get_payload_data_for_item(self , publish):
        return { 
            "ItemCode": self.item_code, "ItemName": self.item_name, "CategoryEN": self.custom_category_en, 
            "CategoryAR": self.custom_category_ar, "CategoryFR": self.custom_category_fr, 
            "BrandEN": self.custom_brand_en, "BrandAR": self.custom_brand_ar, "BrandFR": self.custom_brand_fr, 
            "SubBrand1EN": self.custom_subbrand1_en,  "SubBrand1AR": self.custom_subbrand1_ar,  "SubBrand1FR": self.custom_subbrand1_fr, 
            "SubBrand2EN": self.custom_subbrand2_en,  "SubBrand2AR": self.custom_subbrand2_ar,  "SubBrand2FR": self.custom_subbrand2_fr, 
            "SubBrandPic": self.custom_subbrand_pic_en,  "SubBrandVed": self.custom_subbrand_ved_en,  "ShortDescriptionEN": self.custom_short_disc_en, 
            "ShortDescriptionAR": self.custom_short_disc_ar, "ShortDescriptionFR": self.custom_short_disc_fr, 
            "DescriptionEN": self.custom_long_disc_en,  "DescriptionAR": self.custom_long_disc_ar, "DescriptionFR": self.custom_long_disc_fr, 
            "ProductUseEN": self.custom_product_use_en, "ProductUseAR": self.custom_product_use_ar,  "ProductUseFR": self.custom_product_use_fr, 
            "Surface1EN": self.custom_surface1_en, "Surface1AR": self.custom_surface1_ar, "Surface1FR": self.custom_surface1_fr, 
            "Surface2EN": self.custom_surface2_en,  "Surface2AR": self.custom_surface2_ar, "Surface2FR": self.custom_surface2_fr, 
            "Surface3EN": self.custom_surface3_en,  "Surface3AR": self.custom_surface3_ar, "Surface3FR": self.custom_surface3_fr, 
            "FinishesEN": self.custom_finishes_en, "FinishesAR": self.custom_finishes_ar, "FinishesFR": self.custom_finishes_fr, 
            "Colors": self.custom_colors_en,  "MSDS": self.custom_msds_en,  "TDS": self.custom_tds_en, "Sheen": self.custom_sheen_en, 
            "MetaDescriptionEN": self.custom_metadisc_en, "MetaDescriptionAR": self.custom_metadisc_ar, "MetaDescriptionFR": self.custom_metadisc_fr, 
            "CoveragePerPackEN": self.custom_coverageperpack_en, "CoveragePerPackAR": self.custom_coverageperpack_ar, 
            "CoveragePerPackFR": self.custom_coverageperpack_fr,  "ApplicationToolEN": self.custom_applicationtool_en, 
            "ApplicationToolAR": self.custom_applicationtool_ar, "ApplicationToolFR": self.custom_applicationtool_fr, 
            "PackSizeEN": self.custom_packsize_en, "PackSizeAR": self.custom_packsize_ar, "PackSizeFR": self.custom_packsize_fr, 
            "Publish" : publish
        }

def get_header_data():
    return  {
    'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
    'Content-Type': 'application/json'
    }
    
@frappe.whitelist()
def get_default_image():
        result = frappe.db.sql("""
            SELECT 
               tdi.name, tdi.brand, tdi.is_product, tdi.is_system,
                CASE 
                    WHEN tdi.default_image IS NULL THEN NULL 
                    ELSE CONCAT('https://ugc.kcsc.com.jo', tdi.default_image)
                END AS default_image   
            FROM `tabDefault Image` tdi
            WHERE tdi.publish = 1
        """, as_dict=True)
        return result
