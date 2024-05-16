// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("User Portal", {
    refresh: function(frm) {
        if (frm.doc.docstatus === 1) { 
            frm.add_custom_button(__('Create User Portal'), function(){
                frappe.call({
                    doc: frm.doc,
                    method: 'create_user', 
                    callback: function(r) {
                        frappe.msgprint(r.message);
                    }
                });
            });
        }
    }
});