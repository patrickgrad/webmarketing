from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import App

def index(request):
	return HttpResponse("Hello, world. You're at the account index.") 

def profile(request):
	applist = App.objects.all()
	context = {'applist' : applist}
	return render(request, 'registration/profile.html', context)
