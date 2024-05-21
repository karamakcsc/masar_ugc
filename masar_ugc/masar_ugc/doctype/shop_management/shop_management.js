// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Management", {
    setup: function (frm) {
		frm.set_query("sales_man", function (doc) {
			return {
				filters: [
					['Sales Person', 'is_group', '=', 0],
					['Sales Person', 'enabled', '=', 1]
				]
			};
		});
		frm.set_query("supervisor", function (doc) {
			return {
				filters: [
					['Supervisor', 'is_enable', '=', 1]
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