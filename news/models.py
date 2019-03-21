from django.db import models
from django.utils import timezone
from django.urls import reverse

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='Images/%Y/%m/%d/')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    date_and_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "\"" + self.title + "\" by " + self.author

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})