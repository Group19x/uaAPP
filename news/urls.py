from django.urls import include, path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='news'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete'),
]