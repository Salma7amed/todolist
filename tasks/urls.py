from django.conf.urls import patterns, url
import tasks.views

urlpatterns = [
	url(r'^$', tasks.views.display, name = "task_display"),
	url(r'^task/create/', tasks.views.create, name = "task_create"),
	url(r'^task/resolve/',tasks.views.resolve, name = "task_resolved")

]