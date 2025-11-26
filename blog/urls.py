from django.urls import path
from blog.views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home')
]