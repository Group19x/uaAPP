from django.urls import include, path
from . import views
from .views import LeaderboardCreateView, LeaderboardListView, LeaderboardUpdateView, LeaderboardDeleteView
from django.views.generic import TemplateView

urlpatterns = [
	path('', LeaderboardListView.as_view(extra_context={'sport_class': 'Main'}), name='leaderboard'),
    path('WVB', LeaderboardListView.as_view(extra_context={'sport_class': 'Women\'s Volleyball'}), name='leaderboard-wvb'),
    path('MVB', LeaderboardListView.as_view(extra_context={'sport_class': 'Men\'s Volleyball'}), name='leaderboard-mvb'),
    path('WBB', LeaderboardListView.as_view(extra_context={'sport_class': 'Women\'s Basketball'}), name='leaderboard-wbb'),
    path('MBB', LeaderboardListView.as_view(extra_context={'sport_class': 'Men\'s Basketball'}), name='leaderboard-mbb'),
	path('leaderboard/new/', LeaderboardCreateView.as_view(), name='leaderboard-create'),	
 	path('leaderboard/<int:pk>/update', LeaderboardUpdateView.as_view(), name='leaderboard-update'),
	path('leaderboard/<int:pk>/delete', LeaderboardDeleteView.as_view(), name='leaderboard-delete'),
]