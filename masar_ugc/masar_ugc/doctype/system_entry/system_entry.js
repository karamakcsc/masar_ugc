// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("System Entry", {
    system_brand: function(frm){
        auto_number_sys_no(frm);
    }
});


function auto_number_sys_no(frm) {
    if (frm.doc.system_brand){
        if (frm.doc.system_brand === "Uniguard") {
            frm.doc.system_no = 1100;
        } else if (frm.doc.system_brand === "Jotun") {
            frm.doc.system_no = 2200;
        } else if (frm.doc.system_brand === "Jotun&Uniguard") {
            frm.doc.system_no = 3000;
        } else {
            frm.doc.system_no = null;
        }
        frm.refresh_field("system_no");
    }
}