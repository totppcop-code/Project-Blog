from django.shortcuts import render
from .models import Post, Comment
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm,CommentForm

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-create_date']
  

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.object)
        return context
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    
    
    def get_success_url(self):
        return reverse_lazy('post-list')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post-list')


class PostDeleteView(DeleteView):
    model = Post
  
    def get_success_url(self):
        return reverse_lazy('post-list')    



class CommentListView(ListView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.pk})

class CommentDetailView(DetailView):
    model = Comment    


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
   

    def form_valid(self,form):
        post_id = self.request.POST.get('post')
        form.instance.post = Post.objects.get(pk=post_id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = form.instance.post
        return context


    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.post.pk})


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.post.pk})


class CommentDeleteView(DeleteView):
    model = Comment 

    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.post.pk})


