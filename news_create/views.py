from django.shortcuts import render
from .forms import NewsCreateForm
from django.http import HttpResponseRedirect
from news.models import Article

def NewsCreate(request):
    if request.method == 'POST':
        print("POST")
        form = NewsCreateForm(request.POST, request.FILES)
        if form.is_valid():
            print("VALID")
            form.save()
            #form.save()
            return HttpResponseRedirect('/')
    else:
        print("NOT")
        form = NewsCreateForm()
    return render(request, 'news_create/news_create.html', {'form':form})
