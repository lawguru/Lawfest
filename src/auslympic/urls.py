from django.urls import path
from .views import Home, SportView, LeaderBoard, NoticeView, MerchandiseView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('leaderboard/', LeaderBoard.as_view(), name='leaderboard'),
    path('notices/', NoticeView.as_view(), name='notices'),
    path('merchandise/', MerchandiseView.as_view(), name='merchandise'),
    path('<int:pk>/', SportView.as_view(), name='sport')
]
