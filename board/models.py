from django.db import models


class Board(models.Model):

    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=20)
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

