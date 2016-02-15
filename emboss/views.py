from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import itertools

@login_required
def dashboard(request):
	iterator=itertools.count()
	all_media_list = Media.objects.filter(parent_user=User.objects.get(username=request.user.get_username())).order_by('-date_modified')
	archive_media_list = all_media_list.filter(archive=True)
	latest_media_list = all_media_list.filter(archive=False)[:4]
	all_media_list = all_media_list.filter(archive=False)
	context = {'latest_media_list' : latest_media_list, 'all_media_list':all_media_list, 'archive_media_list':archive_media_list ,'iterator':iterator}
	return render(request, 'emboss/dashboard.html', context)

def splash(request):
	return HttpResponse("Emboss splash page.")

@login_required
def detail(request, media_id):
	context = {}
	return render(request, 'emboss/detail.html', context)

class New(View):
	
	@method_decorator(login_required)
	def get(self, request):
		return render(request, 'emboss/new_home.html', {})

#####################################################################
#
#NewSpecific
#
#View responsible for serving forms to create new pieces of media and
#the storage of the information. This implementation allows the user 
#to interfere with the type of media they save the form as, but since 
#this creates no problems (extra data just goes unused, extra database
#values go unfilled) I'll give users the freedom to make wacky documents.
#
######################################################################

class NewSpecific(View):

	@method_decorator(login_required)
	def get(self, request, media_type):

		if(media_type=="0"):
			form = CouponForm()

		elif(media_type=="1"):
			form = TicketForm()

		elif(media_type=="2"):
			form = InvoiceForm()

		else:
			return HttpResponseRedirect("../")

		return render(request, 'emboss/new_media.html', {"form":form, "media_type":media_type})

	def post(self, request, media_type):

		if(media_type=="0"):
			form = CouponForm(request.POST)

		elif(media_type=="1"):
			form = TicketForm(request.POST)

		elif(media_type=="2"):
			form = InvoiceForm(request.POST)

		else:
			return HttpResponseRedirect("../")

		if form.is_valid():

			username = request.user.get_username()
			print username
			user = User.objects.get(username=username)
					
			try:   #this user only belongs to one account, automatically assign coupon to this account
				account = Account.objects.get(users=user)
				print account
			except MultipleObjectsReturned:   #this user belongs to more than one account, ask which one the new coupon should be for
				accounts = Account.objects.filter(users=user)
				for a in accounts:
					print(a)

			media = form.save(commit=False)
			media.parent_account = account
			media.parent_user = user

			form.save()

			return HttpResponseRedirect("/emboss/")
		return HttpResponseRedirect("/emboss/new/%s", media_type)



@login_required
def edit(request, media_id):
	return HttpResponse("Emboss media edit page.")

def productionWLead(request, media_id, lead_id):
	return HttpResponse("Emboss media view for production. Lead dependent.")

def productionWOLead(request, media_id):
	return HttpResponse("Emboss media view for production. Lead independent.")