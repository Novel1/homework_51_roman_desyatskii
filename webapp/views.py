from random import randint

from django.shortcuts import render, redirect

from webapp.db import DataBase


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def cat_name(request):
    DataBase.context['name'] = request.POST.get('name')
    return name_view(request)


def name_view(request):
    happiness = DataBase.context['happiness']
    if happiness > 60:
        media = 'cat_1.jpg'
    elif happiness > 40:
        media = 'cat_2.jpg'
    elif happiness > 15:
        media = 'cat_3.jpg'
    elif happiness >= 1:
        media = 'cat_4.jpg'
    else:
        media = 'cat_5.jpg'

    cat = {
        'name': DataBase.context['name'],
        'year': DataBase.context['year'],
        'happiness': happiness,
        'eat': DataBase.context['eat'],
        'media': media,
    }
    return render(request, 'inform_cat.html', cat)


def cat_game(request):
    if request.method == 'POST':
        pick = request.POST.get('pick')

        if DataBase.context['happiness'] > 100:
            DataBase.context['happiness'] = 100
        elif DataBase.context['happiness'] < 0:
            DataBase.context['happiness'] = 0

        if DataBase.context['eat'] > 100:
            DataBase.context['eat'] = 100
            DataBase.context['happiness'] -= 30
        elif DataBase.context['eat'] < 0:
            DataBase.context['eat'] = 0
            DataBase.context['happiness'] -= 30

        if pick == 'play_cat':
            if DataBase.context['status'] == 'sleep_cat':
                DataBase.context['status'] = 'play_cat'
                DataBase.context['happiness'] -= 5
            else:
                if randint(1, 3) == 3:
                    DataBase.context['happiness'] = 0
                else:
                    DataBase.context['happiness'] += 15
                    DataBase.context['eat'] -= 10
                DataBase.context['status'] = 'play_cat'
        elif pick == 'eat_cat' and DataBase.context['status'] != 'sleep_cat':
            DataBase.context['eat'] += 15
            DataBase.context['happiness'] += 5
            DataBase.context['status'] = 'eat_cat'
        elif pick == 'sleep_cat':
            DataBase.context['happiness'] += 5
            DataBase.context['eat'] -= 5
            DataBase.context['status'] = 'sleep_cat'

    return redirect('/cat_info_view')

