from django import forms
from .models import Word

class NewWord(forms.ModelForm):
	class Meta:
		model = Word
		fields = [
		'name',
		'description'
		]