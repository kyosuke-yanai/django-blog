from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.db.models import Q

class IndexView(ListView):
    template_name = 'app/index.html'
    model = Post

    def get_queryset(self):
        word = self.request.GET.get('query')
        if word:
            object_list = Post.objects.filter(Q(title__icontains=word) | Q(author__username__icontains=word))
        else:
            object_list = Post.objects.all()
        object_list = object_list.order_by('-id')
        return object_list

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

@require_POST
def CommentDelete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('blog_detail', pk=post_pk)