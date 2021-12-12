from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class IndexView(ListView):
    template_name = 'app/index.html'
    model = Post
    ordering = '-id'

class BlogDetailView(DetailView):
    template_name = 'app/blog_detail.html'
    model = Post