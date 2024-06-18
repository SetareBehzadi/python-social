from django.urls import path
from home.views import HomeView, trigger_404


app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('trigger-404/', trigger_404),
]
