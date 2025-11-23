frappe.ui.form.on('Quotation', {
    onload: function (frm, cdt, cdn) {
        hide_buttons(frm);
    },
    refresh: function (frm, cdt, cdn) {
        hide_buttons(frm);
        create_print_buttons(frm);
    }, 
    tax_category: function(frm){
        frm.refresh_field('tc_name');
        frm.refresh_field('terms');
        if (!frm.doc.tax_category) {
            frm.clear_table('taxes');
            frm.refresh_field('taxes');
        }
    }
 });
 

function create_print_buttons(frm) {
    if (frm.doc.__islocal != 1) {
        const base_url = window.location.origin;
        console.log(base_url);
        frm.add_custom_button(__("Quotation"), function(){
            const url = `${base_url}/printview?doctype=Quotation&name=${frm.doc.name}&trigger_print=1&format=Quotation%20PF&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=en`;
            window.open(url);
        }, __("Print"));
        frm.add_custom_button(__("Proforma"), function(){
            const url = `${base_url}/printview?doctype=Quotation&name=${frm.doc.name}&trigger_print=1&format=Proforma%20Invoice%20PF&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=en`;
            window.open(url);
        }, __("Print"));
    }
}

function hide_buttons(frm) {
    if (!frappe.user.has_role('System Manager')) {
        // cur_frm.fields_dict['items'].grid.wrapper.find('.btn-open-row').hide();
        cur_frm.fields_dict['taxes'].grid.wrapper.find('.btn-open-row').hide();
        frm.fields_dict['items'].grid.on('render', function() {
            frm.fields_dict['items'].grid.wrapper.find('.grid-add-multiple-rows').hide();
        });
        $('button[data-original-title="Print"].btn.btn-default.icon-btn').hide();
    }
}