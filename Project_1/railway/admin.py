from django.contrib import admin
from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ["Username", "Email_Id", "Address", "modified", "created"]


# list_display=["category_id","category_name"]

admin.site.register(Account, AccountAdmin)

class ContactAdmin(admin.ModelAdmin):
	list_display=["Username","Phone_No","modified", "created"]
	"""docstring for ContactAdmin"""
	
admin.site.register(Contact, ContactAdmin)


# Register your models here.
