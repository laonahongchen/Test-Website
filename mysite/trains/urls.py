
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='train_add'),
    path('t/', views.index2, name='train_add_2'),
    path('o/', views.index1, name='train_add_1'),
]
