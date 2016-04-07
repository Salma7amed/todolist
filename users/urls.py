from django.conf.urls import patterns, url
import users.views

urlpatterns = patterns('users.views',
	url(r'^login/', 'login', name = "login"),
	url(r'^logout/', 'logout', name = "logout"),
)