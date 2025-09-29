frappe.ui.form.on('Quotation', {
    onload: function (frm, cdt, cdn) {
        if (!frappe.user.has_role('System Manager')) {
            // cur_frm.fields_dict['items'].grid.wrapper.find('.btn-open-row').hide();
            cur_frm.fields_dict['taxes'].grid.wrapper.find('.btn-open-row').hide();
            frm.fields_dict['items'].grid.on('render', function() {
                frm.fields_dict['items'].grid.wrapper.find('.grid-add-multiple-rows').hide();
            });
        }
    },
    refresh: function (frm, cdt, cdn) {
        if (!frappe.user.has_role('System Manager')) {
            // cur_frm.fields_dict['items'].grid.wrapper.find('.btn-open-row').hide();
            cur_frm.fields_dict['taxes'].grid.wrapper.find('.btn-open-row').hide();
            frm.fields_dict['items'].grid.on('render', function() {
                frm.fields_dict['items'].grid.wrapper.find('.grid-add-multiple-rows').hide();
                
            });
        }
    }, 
    tax_category: function(frm){
        if (!frm.doc.tax_category) {
            frm.clear_table('taxes');
            frm.refresh_field('taxes');
            
        }
    }
 });
 ////////////////////// strat Mohanad  ////////////

 frappe.ui.form.on("Quotation", {
    refresh: function(frm) {
        console.log("dfghjk");
        frm.add_custom_button(("Quotation"), function() {
            console.log("dfghjk");
            var quot= window.open("http://147.182.251.32:8005/printview?doctype=Quotation&name="+cur_frm.doc.name+"&trigger_print=1&format=Proforma%20Invoice%20PF&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=en" )
        });
    }
});

// frappe.ui.form.on("Quotation", {
//     refresh: function(frm) {
//         // Target the specific print button with flex class
//         $('button[data-original-title="Print"].btn.btn-default.icon-btn').hide();
//     }
// });
 ////////////////////// end Mohanad  ////////////