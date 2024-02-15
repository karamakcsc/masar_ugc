// // frappe.ready(function() {
// //     // This code will be executed when the page is fully loaded
    
// //     // Select the email input field using jQuery
// //     var emailInput = $('[data-fieldname="email"]');
    
// //     // Check if the email input field is found
// //     if (emailInput.length > 0) {
// //         // Bind events here 
// //         console.log("in ready");
        
// //         // Attach validation function directly to the email input field's event handler
// //         emailInput.on('blur', function() {
// //             validateEmail($(this).val());
// //         });
// //     } else {
// //         console.error("Email input field not found.");
// //     }
// // });

// // function validateEmail(email) {
// //     console.log("in validate");
// //     frappe.call({
// //         method: "masar_ugc.masar_ugc.web_form.user_register.user_register.validate_user_email",
// //         args: {
// //             email: email,
// //         },
// //         callback: function(r) {
// //             if (r.message === true) {
// //                 frappe.msgprint("Email already exists. Please choose a different one.");
// //                 console.log("response"); 
// //                 // You might need to handle validation logic here based on your requirements
// //             }
// //         }
// //     });
// // }
// /////////////////////////////////////////////////////////////////////////
// frappe.ready(function() {
//     // This code will be executed when the page is fully loaded
    
//     // Select the email input field using jQuery
//     var emailInput = $('[data-fieldname="email"]');
//     if (emailInput.length > 0) {
     
//         var saveButton = $('.submit-btn');
//         saveButton.on('click', function(event) {
//             event.preventDefault();
//             var email = emailInput.val();
//             validateEmail(email);
//             console.log("insave bouttom ");
//         });       
//     } else {
//         console.error("Email input field not found.");
//     }
// });

// function validateEmail(email) {
//     frappe.call({
//         method: "masar_ugc.masar_ugc.web_form.user_register.user_register.validate_user_email",
//         args: {
//             email: email,
//         },
//         callback: function(r) {
//             if (r.message) {
//                 console.log("response");
//             }
//         }
//     });
// }






// ///////////////////////////////////////////////////////////////////////////////

