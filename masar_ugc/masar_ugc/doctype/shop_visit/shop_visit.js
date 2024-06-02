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
// Get the position before calling validate function
navigator.geolocation.getCurrentPosition(function(position) {
    frappe.ui.form.on('Shop Visit', {
        validate: function(frm) {
            if (frm.is_new()) {
                var longitude = position.coords.longitude;
                var latitude = position.coords.latitude;

                frappe.call({
                    type: "GET",
                    url: `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`,
                    callback: function(r) {
                        frm.set_value('country', r.address.country || '');
                        frm.set_value('city', r.address.city || '');
                        frm.set_value('neighbourhood', r.address.neighbourhood || '');
                        frm.set_value('road', r.address.road || '');
                        frm.set_value('house_number', r.address.house_number || '');
                        frm.set_value('full_address', r.display_name || '');
                        frm.set_value('latitude', r.lat);
                        frm.set_value('longitude', r.lon);
                    },
                    error: function(xhr, status, error) {
                        console.error("Error fetching address from coordinates:", status, error);
                    }
                });
            }
        }
    });
});


//         // Get current position
//         navigator.geolocation.getCurrentPosition(onPositionReceived, function(error) {
//             console.error("Error getting current position:", error.message);
//         });
//     }
// });


// // frappe.ready(function() {
// //     frappe.realtime.on("run_js_function", function(data) {
// //         // Call your JavaScript function here
// //         your_js_function();
// //     });
// // });

// // function your_js_function() {
// //     // frappe.msgprint('python');
// //     console.log('python');
// }

