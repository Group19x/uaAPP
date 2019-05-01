from django import forms
from django.contrib.auth.models import User
from news.models import Article

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image', 'title', 'author', 'body', ]
    #image = forms.ImageField()
    #title = forms.CharField(max_length=100)
    #author = forms.CharField(max_length=100)
    #body = forms.CharField()
    #date_and_time = forms.DateTimeField()