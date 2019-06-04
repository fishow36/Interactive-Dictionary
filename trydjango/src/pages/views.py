from django.shortcuts import render
from django.http import HttpResponse
from rus_urban import settings

from words.models import Word

# make_tables(db_name) # uncomment if you want to drop and create new tables

# Create your views here.
def home_view(request, *args, **kwargs):
	# хочу вывести три последних слова пока
	latest_id = Word.objects.latest('id').id
    
	home_context = {
        'word1' : Word.objects.get(id=latest_id),
        'word2' : Word.objects.get(id=latest_id-1),
        'word3' : Word.objects.get(id=latest_id-2)
	}
	return render(request, 'home.html', home_context)

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

    # db.execute('''INSERT INTO word_info (word, definition, updater)
    #               VALUES ("сычиу", "люди, которые <...>фыв", "e12g")''')

	return render(request, 'add.html', context)

def output(request, *args, **kwargs):
    return render(request, 'output.html', {})
