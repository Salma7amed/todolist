from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


def signin(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(data = request.POST)
			next_param = request.GET.get('next', False)
			next_url = next_param if next_param else '/'
			if form.is_valid:
				user = authenticate(username=request.POST['username'], password=request.POST['password'])
				if user is not None:
					if user.is_active:
						login(request, user)
						return redirect(next_url)
		else:
			form = LoginForm()
		return render(request,'users/signin.html', {'form': form})


def signout(request):
	logout(request)
	return redirect(reverse_lazy('users:signin'))
