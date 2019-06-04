from django.shortcuts import render
from django.http import HttpResponse
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



