from django.http import HttpResponseRedirect
from django.shortcuts import render

# 할일 리스트 / 할일 생성 / 할일 삭제
from django.urls import reverse

from article.forms import ArticleForm
from article.models import Article


def create_todo(request):

    lists = Article.objects.all()

    if request.method == 'GET':
        form = ArticleForm()

        return render(request, 'index.html', {
            "form": form,
            "lists": lists,
        })

    if request.method == 'POST':

        form = ArticleForm(request.POST)

        if form.is_valid():
            todo = form.save()
            return HttpResponseRedirect(reverse('create_todo'))
    else:
        form = ArticleForm()

    return render(request, 'index.html', {
        "form": form,
        "lists": lists,
    })


def delete_todo(request, id):

    findTodo = Article.objects.get(id=id)
    findTodo.delete()

    return HttpResponseRedirect(reverse('create_todo'))
