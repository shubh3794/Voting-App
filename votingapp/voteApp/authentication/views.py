from django.shortcuts import render
from .models import Account
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

def user_signup(request):
	if request.method=='POST':
		email = request.POST['email']
		password = request.POST['password']
		username = request.POST['username']
		acc = Account.objects.get(email=email)
		if not acc:
			user = Account.objects.create_user(email,password,{'username':username})
			authenticate(email=email,password=password)
			return HttpResponseRedirect(reverse('polls:index'))
		else:
			acc =authenticate(email=email,password=password)
			if acc.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('polls:index'))
			else:
				return render(request,'polls/signup.html',{'error':'User already exists, login with correct details'})

	else:
		return render(request,'polls/signup.html',{})

		


def user_login(request):
	if request.method =='POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('polls:index'))
			else:
				return render(request,'polls/login.html',{
					'error':'User no longer active'
					})
		else:
			return render(request,'polls/login.html',{
					'error':'invalid details'
					})
	else:
		return render(request,'polls/login.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('polls:index'))
