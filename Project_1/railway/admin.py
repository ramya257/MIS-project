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

class StationAdmin(admin.ModelAdmin):
	list_display=["Station_Code","Station_Name","modified","created"]

admin.site.register(Station, StationAdmin)

class StoppageAdmin(admin.ModelAdmin):
	list_display=["Train_No","Station_Code","Arrival_Time","Departure_Time","modified","created"]

admin.site.register(Stoppage, StoppageAdmin)

class TrainAdmin(admin.ModelAdmin):
    list_display=["Train_No","Name","Seat_Sleeper","Seat_First_Class_AC","Seat_Third_Class_AC",
                  "Wifi","Food","Fare","Run_On_Sunday","Run_On_Monday","Run_On_Tuesday","Run_On_Wednesday",
                  "Run_On_Thursday","Run_On_Friday","Run_On_Saturday","modified","created"]
admin.site.register(Train, TrainAdmin)
# Register your models here.
