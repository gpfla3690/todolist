from django.urls import path

from article import views

urlpatterns = [
    path('', views.create_todo, name='create_todo'),
]