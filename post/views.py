from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(group=None) 

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('post:detail', kwargs={'pk': self.object.pk})
    
def delete_post(request, pk):
    obj = Post.objects.get(pk=pk)

    if request.method == 'POST':
        if obj.created_by == request.user:
            obj.delete()
            return redirect('post:home')
        else:
            messages.error(request, 'You are not authorized to delete this post')
            return redirect('post:home')
    return render(request, 'post/post_confirm_delete.html', {'obj':obj})

@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)
    post.save()
    return redirect(request.META['HTTP_REFERER'])
    

   
    