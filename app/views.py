from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    template_name = 'app/index.html'
    model = Post
    ordering = '-id'

class BlogDetailView(DetailView, FormView):
    template_name = 'app/blog_detail.html'
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(comment_by=Post.objects.get(id=self.kwargs['pk']))
        return context

    def form_valid(self, form):
        form.instance.comment_by = Post.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.kwargs['pk']})

class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'app/blog_create.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogEditView(LoginRequiredMixin, UpdateView):
    template_name = 'app/blog_edit.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('index')

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'app/blog_delete.html'
    model = Post
    success_url = reverse_lazy('index')