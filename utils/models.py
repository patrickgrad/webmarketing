from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from account.models import Account

#collection of an unlimited number of types and quantity of data 
class DataStream(models.Model):
	parent_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	description = models.CharField(max_length=100)
	
#single point of data
class DataPoint(models.Model):
	parent_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	data_stream = models.ManyToManyField(DataStream)
	data = models.FloatField()
	units = models.CharField(max_length=20)
	time = models.DateTimeField()
	flag = models.CharField(max_length=100,blank=True)
