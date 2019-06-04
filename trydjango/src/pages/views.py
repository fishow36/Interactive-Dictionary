from django.shortcuts import render
from django.http import HttpResponse
from rus_urban import settings
<<<<<<< HEAD
# from django.db import connection
from words.models import Word

# make_tables(db_name) # uncomment if you want to drop and create new tables
=======
from django.db import connection
from db_utils import Database
from db_maker import make_tables
from words.models import Word

db_name = settings.DATABASES['default']['NAME']
make_tables(db_name) # uncomment if you want to drop and create new tables
>>>>>>> b4b53b1498b63a74d3a01f0709e2c0f51ae6644a

# Create your views here.
def home_view(request, *args, **kwargs):
	# хочу вывести три последних слова пока
	# latest_id = Word.objects.latest('id').id
    """
	home_context = {
        'word1' : Word.objects.get(id=latest_id),
        'word2' : Word.objects.get(id=latest_id-1),
        'word3' : Word.objects.get(id=latest_id-2)
	}
    """
    home_context = {}
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
    # cursor = connection.cursor()
    # cursor.execute('''...''')
    # row = cursor.fetchone()
<<<<<<< HEAD
=======
    db = Database(db_name)
    row = db.execute('''SELECT * FROM word_info''')
    db.commit()
    print(request.GET, row)
>>>>>>> b4b53b1498b63a74d3a01f0709e2c0f51ae6644a
    return render(request, 'output.html', {})
