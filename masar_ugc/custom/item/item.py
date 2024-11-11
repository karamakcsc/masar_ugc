import frappe


def validate(self, method):
    set_shortdisc(self)

def set_shortdisc(self):
    if self.custom_short_disc_en:
        self.description = self.custom_short_disc_en