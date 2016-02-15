from __future__ import unicode_literals

from django.db import models
from account.models import Account

class LeadInfo(models.Model):
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=50, blank=True)
	phone_number = models.CharField(max_length=10)

class Lead(LeadInfo):
	parent_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	tags = models.CharField(max_length=200, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Template(models.Model):
	name = models.CharField(max_length=50, default="Untitled Template")
	twilio_xml_path = models.CharField(max_length=100)
	isPublic = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Message(models.Model):
	parent_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	twilio_xml_path = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.parent_account.__str__() + " - " + self.twilio_xml_path

class Step(models.Model):
	name = models.CharField(max_length=40, default="Untitled Step")
	next_step = models.CharField(max_length=50, default=-1)
	_filter = models.CharField(max_length=100, blank=True)
	message = models.ForeignKey(Message, on_delete=models.CASCADE, blank=True)
	exe_date = models.DateTimeField('execution date', blank=True)

	def __str__(self):
		return self.name

class Campaign(models.Model):
	name = models.CharField(max_length=50, default="Untitled Campaign")
	parent_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	first_step = models.ForeignKey(Step, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return self.name