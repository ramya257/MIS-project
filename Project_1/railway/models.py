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



# Create your models here.

