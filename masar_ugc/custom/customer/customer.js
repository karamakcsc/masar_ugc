//// Fetching Leave Type with Filter ///// Start ///Siam

frappe.ui.form.on('Customer', {
    setup: function (frm) {
            cur_frm.fields_dict['custom_shop_evaluation'].get_query = function(doc) {
                return {
                    filters: {
                        // "report_type": "Profit and Loss",
                        "is_enable": 1,
                    }
                };
            };
    }
});

frappe.ui.form.on('Customer', {
    setup: function (frm) {
            cur_frm.fields_dict['custom_shop_sector'].get_query = function(doc) {
                return {
                    filters: {
                        // "report_type": "Profit and Loss",
                        "is_enable": 1,
                    }
                };
            };
    }
});
frappe.ui.form.on('Customer', {
    setup: function (frm) {
            cur_frm.fields_dict['custom_signboard_type'].get_query = function(doc) {
                return {
                    filters: {
                        // "report_type": "Profit and Loss",
                        "is_enable": 1,
                    }
                };
            };
    }
});
