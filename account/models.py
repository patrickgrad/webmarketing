from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
#from emboss.models import EmbossData

class BasicInfo(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=10, blank=True)

class Account(BasicInfo):
	users = models.ManyToManyField(User)
	business_name = models.CharField(max_length=20, blank=True)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zip_code = models.CharField(max_length=5)
	stripe_id = models.CharField(max_length=200, blank=True)
	bank_id = models.CharField(max_length=200, blank=True)
	outstanding_balance = models.IntegerField(default=0)

	#emboss_data = models.ForeignKey(EmbossData, on_delete=models.CASCADE)

	def __str__(self):
		if(self.business_name != ""):
			return self.business_name
		else:
			return self.first_name + " " + self.last_name

class App(models.Model):
	human_name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)

	def __str__(self):
		return self.human_name