# urls.py in the front app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]