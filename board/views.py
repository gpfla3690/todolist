from django.shortcuts import render

# Create your views here.
from board.models import Board


def board_list(request):
    boards = Board.objects.all()

    return render(request, 'boardList.html', {
        'boards': boards,
    })