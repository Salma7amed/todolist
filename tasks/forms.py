from django import forms

class CreateTaskForm(forms.Form):
	title = forms.CharField(
		widget= forms.TextInput(attrs={'data-trigger':'change', 'data-minlength':'3','data-required':'true', 
			'placeholder':'Add a to-do ..', 'class':'form-control',}), label=("Title:")
        )

