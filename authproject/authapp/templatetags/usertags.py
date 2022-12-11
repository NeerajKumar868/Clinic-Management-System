from django import template
register=template.Library()

def isAdmin(user):
    return user.groups.filter(name="admin").exists()

def isCustomer(user):
    return user.groups.filter(name="customer").exists()

register.filter("admin",isAdmin)
register.filter("customer",isCustomer)

