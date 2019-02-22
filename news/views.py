from django.shortcuts import render
from .models import Article

'''
Passes to news/news.html the table Article
'''

def Something(request):
    context = {
        'news' : Article.objects.all()
    }
    return render(request, 'news/news.html', context) 