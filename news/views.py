from django.shortcuts import render
from .models import Article
from django.views.generic import ListView

'''
Passes to news/news.html the table Article
'''

def Something(request):
    context = {
        'news' : Article.objects.all()
    }

    if request.method == 'POST':
        print("POST")
        id_list = Article.objects.all().values_list('id', flat=True)
        for id in id_list:
            print("Test", id)
            if request.POST.get(str(id)):
                print(id)
                Article.objects.get(id=id).delete()

    return render(request, 'news/news.html', context)

class ArticleListView(ListView):
    model = Article
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-date_and_time']
