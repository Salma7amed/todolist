from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .models import *
from .forms import CreateTaskForm

#@login_required(login_url=reverse('signin'))
def list(request):
	try:
		tasklist = Task.objects.filter(owner = request.user)
		print tasklist
		return render(request,'tasks/list.html', { 'usertasks': tasklist, 'form': CreateTaskForm()})
	except Exception, e:
		raise e

def create(request):
	if request.method == 'POST':
		form = CreateTaskForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			newtask = Task.objects.create(title = title, done = False, owner = request.user)
			newtask.save()
			print newtask
	return redirect('/task/list')

def resolve(request):
	pass

