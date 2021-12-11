from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class IndexView(ListView):
    template_name = 'app/index.html'
    model = Post
    ordering = '-id'