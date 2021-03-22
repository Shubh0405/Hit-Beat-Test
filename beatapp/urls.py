from django.urls import path
from . import views

app_name = 'beatapp'

urlpatterns = [
    path('userpost/',views.UserDetails,name='userpost'),
    path('userget/<int:pk>/',views.UserGetDetails,name='userget'),
    path('beatsget/',views.BeatGetDetails,name='beatsget'),
    path('useraudiopost/',views.UserAudioPost,name='useraudiopost'),
    path('userscoreget/<int:pk>',views.UserScoreGet,name='userscoreget'),
]
