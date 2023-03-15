from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ask_ai/', views.ask_ai, name='ask_ai'),
]