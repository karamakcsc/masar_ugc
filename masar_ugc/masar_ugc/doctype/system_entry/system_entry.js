// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("System Entry", {
    system_brand: function(frm){
        auto_number_sys_no(frm);
    },
});


function auto_number_sys_no(frm) {
    if (frm.doc.system_brand) {
        frappe.call({
            doc: frm.doc,
            method: "get_max_system_no",
            callback: function (r) {
                if (r.message) {
                    frm.set_value("system_no", r.message);
                } else {
                    frm.doc.system_no = null;
                }
            }
        });
        frm.refresh_field("system_no");
    }
}