// Copyright (c) 2024, KCSC and contributors
// For license information, please see license.txt
// frappe.ui.form.on("User Register", {
//     refresh(frm) {
//     },
//     on_submit: function (frm) {
//         frappe.call({
//             method: "masar_ugc.masar_ugc.doctype.user_register.user_register.createdoc",
//             args: {
//                 you_are: frm.doc.you_are,
//                 first_name_en: frm.doc.first_name_en,
//                 middle_name_en: frm.doc.middle_name_en,
//                 last_name_en: frm.doc.last_name_en,
//                 register_date: frm.doc.register_date,
//                 email: frm.doc.email
//             },
//             callback: function (r) {
//                 frappe.msgprint(r.message);
//         }
//     });
//     }
// });

///////////////////////////////////////////////////////////////////////////

// frappe.ui.form.on("User Register", {
//     refresh(frm) {

//     },
//     on_submit: function (frm) {
//         frappe.call({
//             method: "masar_ugc.masar_ugc.doctype.user_register.user_register.createdoc",
//             args: {
//                 you_are: frm.doc.you_are,
//                 first_name_en: frm.doc.first_name_en,
//                 middle_name_en: frm.doc.middle_name_en,
//                 last_name_en: frm.doc.last_name_en,
//                 register_date: frm.doc.register_date,
//                 email: frm.doc.email
//             },
//             callback: function (r) {
//                 frappe.msgprint(r.message);
//             }
//         });
//     }
// });