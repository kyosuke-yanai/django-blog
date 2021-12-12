from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="タイトル", max_length=50)
    text = models.TextField(verbose_name="本文", max_length=1000)
    created = models.DateTimeField(verbose_name="投稿日", auto_now_add=True)

    def __str__(self):
        return self.title