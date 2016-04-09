from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
	title = models.CharField(blank=True, max_length=200)
	done = models.BooleanField(default=False)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
