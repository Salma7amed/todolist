from django.forms import ModelForm, TextInput, ValidationError
from .models import Task

class CreateTaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['title']
		widgets = {
			'title' : TextInput(attrs={'id':'task_title', 'data-minlength':'3','data-required':'true', 
			'placeholder':'Add a to-do ..', 'class':'form-control', 'autocomplete':'off',}),
		}

	def clean_title(self):
		title = self.cleaned_data.get('title', None)
		if not title or title.isspace():
			print 'validators'
			raise ValidationError('Task title cannot be blank')
		return self.cleaned_data.get('title', None)
