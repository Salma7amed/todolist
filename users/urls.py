from django.conf.urls import patterns, url
import users.views

urlpatterns = [
	url(r'^signin/', users.views.signin, name = "signin"),
	url(r'^signout/', users.views.signout, name = "signout"),
]