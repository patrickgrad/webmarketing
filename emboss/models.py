from __future__ import unicode_literals
from django.utils import timezone
from account.models import Account
from django.contrib.auth.models import User

from django.db import models
from django.forms import ModelForm

from utils.models import DataStream, DataPoint


#global data for the account's media (not user's)
class EmbossData(models.Model):	
	daily_agg = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')				#today's running data
	weekly_agg = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')				#past 7 days running data
	monthly_agg = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')				#past 30 days running data

	weekly_agg_daily = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')		#a week's worth of data, aggragated daily

	monthly_agg_daily = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')		#a month's worth of data, aggragated daily
	monthly_agg_weekly = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')		#a month's worth of data, aggragated weekly

	yearly_agg_weekly = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')		#a year's worth of data, aggragated weekly
	yearly_agg_monthly = models.ForeignKey(DataStream, on_delete=models.CASCADE, related_name='+')		#a year's worth of data, aggragated monthly

class Media(models.Model):
	name = models.CharField(max_length=50,default="Untitled")
	parent_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	parent_user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_modified = models.DateTimeField()
	archive = models.BooleanField(default=0)

	consumed = models.BooleanField(default=0) #or paid in the case of the invoice

	fine_print = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		''' On save, update timestamp '''
		self.date_modified = timezone.now()
		return super(Media, self).save(*args, **kwargs)

class Coupon(Media):
	offer = models.CharField(max_length=30, blank=True)

class CouponForm(ModelForm):

	class Meta:
		model = Coupon
		fields = ['name', 'offer', 'fine_print']

class Ticket(Media):
	venue = models.CharField(max_length=30, blank=True)

class TicketForm(ModelForm):
	class Meta:
		model = Ticket
		fields = ['name', 'venue', 'fine_print']

class Invoice(Media):
	client_name = models.CharField(max_length=30, blank=True)

class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'client_name', 'fine_print']