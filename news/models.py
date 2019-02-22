from django.db import models

class Article(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    date_and_time = models.DateTimeField()
    
    def __str__(self):
        return "\"" + self.title + "\" by " + self.author