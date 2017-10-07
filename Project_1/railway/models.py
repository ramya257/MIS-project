from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
	Username=models.CharField(max_length=30,null=False,blank=True,primary_key=True)
	Password=models.CharField(max_length=30,null=False,blank=True)
	Email_Id=models.EmailField()
	Address=models.CharField(max_length=60,default=None,blank=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return str(self.Username)

class Contact(models.Model):
	Username=models.ForeignKey(Account,db_column="Account.Username",on_delete=models.CASCADE)
	Phone_No=models.CharField(max_length=10,null=False,default='',primary_key=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

	
class Stoppage(models.Model):
	Train_No=models.ForeignKey(Train,db_column="Train.Train_No",max_length=6,default=0,null=False,primary_key=True,on_delete=models.CASCADE)
	Station_Code=models.ForeignKey(Station,db_column="Station.Station_Code",max_length=5,null=False,default='',primary_key=True,on_delete=models.CASCADE)
	Arrival_Time=models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True)
	Departure_Time=models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

class Station(models.Model):
	Station_Code=models.CharField(max_length=10,null=False,default='',primary_key=True)
	Station_Name=models.CharField(max_length=30,null=False)




# Create your models here.

