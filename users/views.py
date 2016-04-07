from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
		else:
			print("The password is valid, but the account has been disabled!")
	else:
		print("The username and password were incorrect.")


def logout(request):
	logout(request)
