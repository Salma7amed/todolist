from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def signin(request):
	if request.user.is_authenticated():
		return redirect('/task/list')
	else:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			print 'signin \n'
			print user
			if user is not None:
				if user.is_active:
					login(request, user)
					print user
					return redirect('/task/list')
				else:
					print("The password is valid, but the account has been disabled!")
			else:
				print("The username and password were incorrect.")
		else:
			print 'must render'
			return render(request,'users/signin.html', {'form': LoginForm()})


def signout(request):
	logout(request)
	return redirect('/user/signin')
