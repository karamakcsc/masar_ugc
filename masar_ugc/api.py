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
                            item_code ,item_name, custom_visible ,custom_sold ,custom_category_en ,
                            custom_category_ar ,custom_category_fr ,custom_brand_en ,custom_brand_ar ,custom_brand_fr ,custom_subbrand1_en ,
                            custom_subbrand1_ar ,custom_subbrand1_fr ,custom_subbrand2_en , custom_subbrand2_ar , custom_subbrand2_fr , 
                            custom_short_disc_en ,
                            custom_short_disc_ar ,custom_short_disc_fr ,custom_product_use_en ,custom_product_use_ar ,custom_product_use_fr ,custom_surface1_en ,custom_surface2_en ,
                            custom_surface3_en ,custom_surface1_ar , custom_surface2_ar ,custom_surface3_ar ,custom_surface1_fr ,custom_surface2_fr ,custom_surface3_fr ,custom_finishes_en , custom_finishes_ar ,custom_finishes_fr ,
                            custom_colors_en ,custom_colors_ar ,custom_colors_fr ,custom_sheen_en ,custom_sheen_ar ,custom_sheen_fr ,
                            custom_packsize_en ,custom_packsize_ar ,custom_packsize_fr ,custom_coverageperpack_en ,custom_applicationtool_en ,custom_coverageperpack_ar ,custom_applicationtool_ar ,
                            custom_coverageperpack_fr , custom_applicationtool_fr , custom_subbrand_pic_en ,custom_subbrand_pic_ar ,
                            custom_subbrand_pic_fr ,custom_subbrand_ved_en , custom_tds_en ,custom_msds_en ,custom_subbrand_ved_ar ,
                            custom_tds_ar ,custom_msds_ar ,custom_subbrand_ved_fr ,custom_tds_fr ,custom_msds_fr ,custom_metadisc_en ,
                            custom_metadisc_ar ,custom_metadisc_fr , custom_long_disc_en ,custom_long_disc_ar ,custom_long_disc_fr ,
                            custom_applicationtool_2_en , custom_applicationtool_2_ar , custom_applicationtool_2_fr, custom_applicationtool_3_en , 
                            custom_applicationtool_3_ar , custom_applicationtool_3_fr , custom_friendly_url, 
                            CASE 
                                    WHEN image IS NULL THEN NULL ELSE CONCAT('https://ugc.kcsc.com.jo', image)
                            END AS image_url
                        FROM tabItem ti
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

##s
@frappe.whitelist()
def get_system_master():
    data = frappe.db.sql("""
        SELECT 
            tse.name AS system_name, tse.system_no, tse.area_of_use_en, tse.area_of_use_ar, tse.area_of_use_fr, 
            tse.area_of_use_en_2, tse.area_of_use_ar_2, tse.area_of_use_fr_2, 
            tse.area_of_use_en_3, tse.area_of_use_ar_3, tse.area_of_use_fr_3, 
            tse.area_of_use_metadiscen, tse.area_of_use_metadiscar, tse.area_of_use_metadiscfr, 
            tse.sub_area_of_use_en, tse.sub_area_of_use_ar, tse.sub_area_of_use_fr, 
            tse.system_brand, tse.system_name_en, tse.system_name_ar, tse.system_name_fr, 
            tse.system_image_link, tse.system_video_link, tse.test_result_link, 
            tse.statement_link, tse.system_metadisc_en, tse.system_metadisc_ar, tse.system_metadisc_fr, 
            tse.system_description_en, tse.system_description_ar, tse.system_description_fr, 
            CASE 
                WHEN tse.image IS NULL THEN NULL 
                ELSE CONCAT('https://ugc.kcsc.com.jo', tse.image) 
            END AS image_url, 
            tpsi.name AS proposed_system_item_name, tpsi.coat, tpsi.no_coat, tpsi.item_code, 
            ti.custom_subbrand2_en
        FROM 
            `tabSystem Entry` tse
        LEFT JOIN 
            `tabProposed System Item` tpsi 
            ON tse.name = tpsi.parent
        LEFT JOIN 
            `tabItem` ti 
            ON tpsi.item_code = ti.name
        WHERE 
            tse.is_published = 1 
            AND tse.workflow_state = 'Publish'
        ORDER BY 
            tse.name
    """, as_dict=True)

    systems = {}
    for row in data:
        system_name = row['system_name']
        if system_name not in systems:
            # Initialize system entry
            systems[system_name] = {
                "name": row["system_name"],
                "system_no": row["system_no"],
                "area_of_use_en": row["area_of_use_en"],
                "area_of_use_ar": row["area_of_use_ar"],
                "area_of_use_fr": row["area_of_use_fr"],
                "system_image_link": row["system_image_link"],
                "system_video_link": row["system_video_link"],
                "image_url": row["image_url"],
                "proposed_system_items": []
            }
        
        # Add child items if they exist
        if row["proposed_system_item_name"]:
            systems[system_name]["proposed_system_items"].append({
                "name": row["proposed_system_item_name"],
                "coat": row["coat"],
                "no_coat": row["no_coat"],
                "item_code": row["item_code"],
                "custom_subbrand2_en": row["custom_subbrand2_en"]
            })

    # Return the grouped data as a list
    return list(systems.values())




@frappe.whitelist()
def get_item(item_code = None):
    cond = None
    if item_code:
        cond = f""" AND item_code = '{item_code}'"""
    return frappe.db.sql(f"""
                         SELECT 
                            item_code ,item_name, custom_visible ,custom_sold ,custom_category_en ,
                            custom_category_ar ,custom_category_fr ,custom_brand_en ,custom_brand_ar ,custom_brand_fr ,custom_subbrand1_en ,
                            custom_subbrand1_ar ,custom_subbrand1_fr ,custom_subbrand2_en , custom_subbrand2_ar , custom_subbrand2_fr , 
                            custom_short_disc_en ,
                            custom_short_disc_ar ,custom_short_disc_fr ,custom_product_use_en ,custom_product_use_ar ,custom_product_use_fr ,custom_surface1_en ,custom_surface2_en ,
                            custom_surface3_en ,custom_surface1_ar , custom_surface2_ar ,custom_surface3_ar ,custom_surface1_fr ,custom_surface2_fr ,custom_surface3_fr ,custom_finishes_en , custom_finishes_ar ,custom_finishes_fr ,
                            custom_colors_en ,custom_colors_ar ,custom_colors_fr ,custom_sheen_en ,custom_sheen_ar ,custom_sheen_fr ,
                            custom_packsize_en ,custom_packsize_ar ,custom_packsize_fr ,custom_coverageperpack_en ,custom_applicationtool_en ,custom_coverageperpack_ar ,custom_applicationtool_ar ,
                            custom_coverageperpack_fr , custom_applicationtool_fr , custom_subbrand_pic_en ,custom_subbrand_pic_ar ,
                            custom_subbrand_pic_fr ,custom_subbrand_ved_en , custom_tds_en ,custom_msds_en ,custom_subbrand_ved_ar ,
                            custom_tds_ar ,custom_msds_ar ,custom_subbrand_ved_fr ,custom_tds_fr ,custom_msds_fr ,custom_metadisc_en ,
                            custom_metadisc_ar ,custom_metadisc_fr , custom_long_disc_en ,custom_long_disc_ar ,custom_long_disc_fr ,
                            custom_applicationtool_2_en , custom_applicationtool_2_ar , custom_applicationtool_2_fr, custom_applicationtool_3_en , 
                            custom_applicationtool_3_ar , custom_applicationtool_3_fr , custom_friendly_url,  
                         CASE 
                                WHEN image IS NULL THEN NULL ELSE CONCAT('https://ugc.kcsc.com.jo', image)
                         END AS image_url

                        FROM tabItem ti
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