from django.shortcuts import render
from django.http import HttpResponse
from .models import Word
from .forms import NewWord
# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, 'home.html', {})

def contacts(request, *args, **kwargs):
	about_context = {
	"about_title" : "Contacts",
	"number" : 18,
	"some_list" : [12, 13, 14, 15]
	}
	return render(request, 'contacts.html', about_context)

def add_word_view(request, *args, **kwargs):
	form = NewWord(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
	'form' : form
	}


	return render(request, 'add.html', context)