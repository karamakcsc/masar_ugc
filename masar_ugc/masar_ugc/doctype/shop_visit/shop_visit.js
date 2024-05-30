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
frappe.ui.form.on('Shop Visit', {
    before_save: function(frm) {
        function onPositionReceived(position) {
            var longitude = position.coords.longitude;
            var latitude = position.coords.latitude;
            console.log("Longitude:", longitude);
            console.log("Latitude:", latitude);
            frappe.call({
                type: "GET",
                url: `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`,
                callback: function(r) {
                    if (r) {
                        frappe.call({
                            doc:frm.doc,
                            method : 'get_current_location_details' , 
                            args :{
                                country :r.address.country , 
                                city  : r.address.city , 
                                neighbourhood :  r.address.neighbourhood, 
                                road :  r.address.road,
                                house_number :  r.address.house_number ,  
                                full_address :  r.address.display_name,
                                lat :  r.address.lat,
                                lon :  r.address.lon
                            }
                        })
                    } else {
                        console.log("Error: Failed to get address from coordinates");
                    }
                }
            });
        }

        // Get current position
        navigator.geolocation.getCurrentPosition(onPositionReceived, function(error) {
            console.error("Error getting current position:", error.message);
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

