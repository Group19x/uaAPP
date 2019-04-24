from django.urls import include, path
from . import views
from .views import LeaderboardCreateView, LeaderboardListView, LeaderboardUpdateView, LeaderboardDeleteView
from .models import Leaderboard

urlpatterns = [
	path('', LeaderboardListView.as_view(extra_context={'sports':Leaderboard.objects.values_list('sport', flat=True).distinct()}), name='leaderboard'),
	path('leaderboard/new/', LeaderboardCreateView.as_view(), name='leaderboard-create'),	
 	path('leaderboard/<int:pk>/update', LeaderboardUpdateView.as_view(), name='leaderboard-update'),
	path('leaderboard/<int:pk>/delete', LeaderboardDeleteView.as_view(), name='leaderboard-delete'),
]