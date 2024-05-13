// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("User Register", {
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

//// Fetching Leave Type with Filter ///// Start ///Siam

frappe.ui.form.on('User Register', {
    setup: function (frm) {
            cur_frm.fields_dict['customer_evaluation'].get_query = function(doc) {
                return {
                    filters: {
                        // "report_type": "Profit and Loss",
                        "is_enable": 1,
                    }
                };
            };
    }
});

frappe.ui.form.on('User Register', {
    setup: function (frm) {
            cur_frm.fields_dict['customer_sector'].get_query = function(doc) {
                return {
                    filters: {
                        // "report_type": "Profit and Loss",
                        "is_enable": 1,
                    }
                };
            };
    }
});
frappe.ui.form.on('User Register', {
    setup: function (frm) {
            cur_frm.fields_dict['signboard_type'].get_query = function(doc) {
                return {
                    filters: {
                        // "report_type": "Profit and Loss",
                        "is_enable": 1,
                    }
                };
            };
    }
});

//// Fetching Leave Type with Filter ///// END ///Siam