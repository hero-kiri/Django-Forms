from django.urls import path
from . import views

urlpatterns = [
    # Вариант 1
   path('', views.index, name='index'),

    # Вариант 2
   path('index2', views.index2, name='index2'),

    # Вариант 3
   path('index3', views.index3, name='index3')
]