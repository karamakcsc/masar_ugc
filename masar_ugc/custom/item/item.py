import frappe


def validate(self, method):
    set_shortdisc(self)
    publish_to_web(self)

def set_shortdisc(self):
    if self.custom_short_disc_en:
        self.description = self.custom_short_disc_en
        

def publish_to_web(self):
    if self.workflow_state == "Publish":
        self.custom_is_publish = 1
        # self.save()
        if self.custom_is_publish:
            frappe.msgprint(f"Item: {self.name}, is published", alert=True, indicator="green")
    else:
        self.custom_is_publish = 0