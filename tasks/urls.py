from django.conf.urls import patterns, url
import tasks.views

urlpatterns = [
	url(r'^list/', tasks.views.list, name = "task_list"),
	url(r'^create/', tasks.views.create, name = "task_create"),
	url(r'^resolve/',tasks.views.resolve, name = "task_resolved")

]