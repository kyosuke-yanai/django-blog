from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=50)
    text = models.TextField(verbose_name="本文", max_length=1000)
    created = models.DateTimeField(verbose_name="投稿日", auto_now_add=True)

    def __str__(self):
        return self.title