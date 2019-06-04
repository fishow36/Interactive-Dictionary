from django.shortcuts import render
from .models import Word
from .forms import NewWord


def add_word_view(request, *args, **kwargs):
	form = NewWord(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
	'form' : form
	}
	return render(request, 'add.html', context)