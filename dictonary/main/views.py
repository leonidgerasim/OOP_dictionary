from django.shortcuts import render
import pandas as pd
import csv
from .forms import WordForm

# Create your views here.


def index(request):
    # df = pd.DataFrame({'Слово': [], 'Перевод': []})
    # df.to_csv('table.csv')
    context = {'title': 'Домашняя страница'}
    return render(request, 'main/index.html', context)


def words_list(request):
    with open('table.csv', 'r', encoding='utf-8') as file:
        table = csv.reader(file)
        m = []
        for i in table:
            m.append((i[1], i[2]))
        context = {'title': 'Список слов',
                   'table': m}
    return render(request, 'main/words_list.html', context)


def add_word(request):
    error = ''
    if request.method == 'POST':
        form = WordForm(data=request.POST)
        if form.is_valid():
            word = form.cleaned_data.get('word')
            p = form.cleaned_data.get('p')
            table = pd.read_csv('table.csv', encoding='utf-8')
            table.loc[len(table.index)] = [len(table.index), word, p]
            table.to_csv('table.csv')
    else:
        form = WordForm()

    context = {'title': 'Добавить запись',
               'form': form
               }
    return render(request, 'main/add_word.html', context)
