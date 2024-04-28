// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Customer Managment", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Customer Managment', {
	setup: function (frm) {
		frm.set_query("sales_man", function (doc) {
			return {
				filters: [
					['Sales Person', 'is_group', '=', 1],
					['Sales Person', 'enabled', '=', 1]
				]
			};
		});
		frm.set_query("supervisor", function (doc) {
			return {
				filters: [
					['Sales Person', 'enabled', '=', 1]
				]
			};
		});
		frm.set_query("district", function (doc) {
			return {
				filters: [
					['District', 'is_enable', '=', 1]
				]
			};
		});
	},
});