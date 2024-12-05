frappe.ui.form.on('Employee', {
    refresh: function(frm) {
        hide_fields(frm);
    },
    onload: function(frm){
        hide_fields(frm);
    },
    setup: function(frm){
        hide_fields(frm);
    }
  });


function hide_fields(frm){
    if (!frappe.user.has_role('System Manager')){
        $('a.nav-link:contains("Connections")').parent('.nav-item').hide();
        // frm.toggle_display("connections_tab", false);
        frm.toggle_display("erpnext_user", false);
        frm.toggle_display("company_details_section", false);
    }
}