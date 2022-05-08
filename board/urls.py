from django.urls import path

from board import views

urlpatterns = [
    path('board/', views.board_list, name='board_list')
]