from django.db import models
from django.utils import timezone
from django.urls import reverse

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Images/%Y/%m/%d/', verbose_name='Image')
    title = models.CharField(max_length=100, verbose_name='News Title')
    author = models.CharField(max_length=100, verbose_name='Author')
    body = models.TextField(verbose_name='Body')
    date_and_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "\"" + self.title + "\" by " + self.author

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})