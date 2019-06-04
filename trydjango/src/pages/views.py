from django.shortcuts import render
from django.http import HttpResponse
from rus_urban import settings
# from django.db import connection
from db_utils import Database
from db_maker import make_tables

db_name = settings.DATABASES['default']['NAME']
# make_tables(db_name) # uncomment if you want to drop and create new tables

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

    # db.execute('''INSERT INTO word_info (word, definition, updater)
    #               VALUES ("сычиу", "люди, которые <...>фыв", "e12g")''')

	return render(request, 'add.html', context)

def output(request, *args, **kwargs):
    # cursor = connection.cursor()
    # cursor.execute('''...''')
    # row = cursor.fetchone()
    db = Database(db_name)
    row = db.execute('''SELECT * FROM word_info''')
    db.commit()
    print(request.GET['word'], row)
    return render(request, 'output.html', {})
