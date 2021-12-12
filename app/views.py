from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    template_name = 'app/index.html'
    model = Post
    ordering = '-id'

class BlogDetailView(DetailView):
    template_name = 'app/blog_detail.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'app/blog_create.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

class BlogEditView(LoginRequiredMixin, UpdateView):
    template_name = 'app/blog_edit.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('index')

class BlogDeleteView(DeleteView):
    template_name = 'app/blog_delete.html'
    model = Post
    success_url = reverse_lazy('index')