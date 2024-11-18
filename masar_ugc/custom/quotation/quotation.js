frappe.ui.form.on('Quotation', {
    onload: function (frm, cdt, cdn) {
        if (!frappe.user.has_role('System Manager')) {
            cur_frm.fields_dict['items'].grid.wrapper.find('.btn-open-row').hide();
            cur_frm.fields_dict['taxes'].grid.wrapper.find('.btn-open-row').hide();
            frm.fields_dict['items'].grid.on('render', function() {
                frm.fields_dict['items'].grid.wrapper.find('.grid-add-multiple-rows').hide();
            });
        }
    },
    refresh: function (frm, cdt, cdn) {
        if (!frappe.user.has_role('System Manager')) {
            cur_frm.fields_dict['items'].grid.wrapper.find('.btn-open-row').hide();
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