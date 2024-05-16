// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Visit", {
    setup: function (frm) {
        frm.set_query("shop_management", function (doc) {
            return {
                filters: [
                    ['Shop Management', 'docstatus', '=', 1]
                ]
            };
        });
    }
});

// frappe.ready(function() {
//     frappe.realtime.on("run_js_function", function(data) {
//         // Call your JavaScript function here
//         your_js_function();
//     });
// });

// function your_js_function() {
//     // frappe.msgprint('python');
//     console.log('python');
// }

