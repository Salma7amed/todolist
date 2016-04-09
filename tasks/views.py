from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import *
from .forms import CreateTaskForm

login_url = reverse_lazy('users:signin')

@login_required(login_url=login_url)
@require_GET
def display(request):
	try:
		tasklist = Task.objects.filter(owner = request.user)
		donetasks = tasklist.filter(done = True)
		todotasks = tasklist.filter(done = False)
		return render(request,'tasks/list.html', { 'donetasks': donetasks, 'todotasks': todotasks, 'form': CreateTaskForm()})
	except Exception, e:
		raise e

@login_required(login_url=login_url)
@require_POST
def create(request):
	task = Task(owner = request.user)
	form = CreateTaskForm(request.POST, instance = task)
	if form.is_valid():
		task = form.save()
		return JsonResponse({ 'id': str(task.id), 'title': task.title })
	return HttpResponse('Invalid Input', status = 422)
	
@login_required(login_url=login_url)
@require_POST
def resolve(request):
	task_id = request.POST.get('id')
	done = request.POST.get('done')
	task = Task.objects.get(id = task_id)
	if done == 'true':
		task.done = True
	else:
		task.done = False
	task.save()
	return JsonResponse({ 'id': str(task_id), 'done': task.done })

