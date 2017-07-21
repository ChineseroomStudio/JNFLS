from django import forms


class NewPostForm(forms.Form):
	title = forms.CharField(max_length=100)
	content = forms.TextInput()
