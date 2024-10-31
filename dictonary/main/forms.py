from django import forms


class WordForm(forms.Form):
    word = forms.CharField(max_length=50)
    p = forms.CharField(max_length=50)

