// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt
frappe.ui.form.on("Customers Visits", {
    setup: function (frm) {
        frm.set_query("customer_management", function (doc) {
            return {
                filters: [
                    ['Customer Management', 'docstatus', '=', 1]
                ]
            };
        });
    }
});
