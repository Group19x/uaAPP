from django.urls import include, path
from .views import (
	SchedPostListView, 
	SchedPostDetailView, 
	SchedPostUpdateView, 
	SchedPostDeleteView
)
from . import views
'''
First Path: Schedule Home
Second Path: Schedule post more in-depth details
Third Path: Schedule Create
Fourth Path: Schedule Update/Edit
Fifth Path: Schedule Delete

Paths 2,4,5 requires model id which is int:pk
'''
urlpatterns = [
    path('', SchedPostListView.as_view(), name='sched'),
    path('post/new/', views.SchedPostCreateView, name='post-create'),
    path('post/<int:pk>/', SchedPostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', SchedPostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', SchedPostDeleteView.as_view(), name='post-delete'),
]