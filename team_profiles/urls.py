from django.urls import include, path
from .views import (
	TeamListView, 
	TeamDetailView,
	TeamCreateView,
	TeamUpdateView,
	TeamDeleteView,
	PlayerCreateView,
	PlayerDeleteView,
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
    path('', TeamListView.as_view(), name='teams'),
    path('<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('new/', TeamCreateView.as_view(), name='team-create'),
    path('<int:pk>/update/', TeamUpdateView.as_view(), name='team-update'),
	path('<int:pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),
	path('player/new/', PlayerCreateView.as_view(), name='player-create'),
	path('<int:pk>/player/delete/', PlayerDeleteView.as_view(), name='player-delete'),
]