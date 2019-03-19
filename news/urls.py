from django.urls import include, path
from . import views
from .views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='news'),
]