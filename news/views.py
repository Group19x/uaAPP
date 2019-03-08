from django.shortcuts import render
from .models import Article

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