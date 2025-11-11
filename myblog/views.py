from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.views import View


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-create_date']
  

class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # 留言區用
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.object)
        # 留言分頁用
        comments = Comment.objects.filter(post=self.object).order_by('-create_date')
        paginator = Paginator(comments,2)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['comments'] = page_obj.object_list
        context['page_obj'] = page_obj

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


class CommentCreateView(SuccessMessageMixin,CreateView):
    model = Comment
    form_class = CommentForm
    success_message = "新增一則留言"
   

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


class CommentUpdateView(SuccessMessageMixin,UpdateView):
    model = Comment
    form_class = CommentForm
    success_message = '更新留言'

    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.post.pk})


class CommentDeleteView(SuccessMessageMixin,DeleteView):
    model = Comment 
    success_message = '刪除一則留言'

    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.post.pk})


class ToggleLikeView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post,pk=pk)
        if request.user in post.like.all():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)
        return redirect(post.get_absolute_url())
    
class ToggleFavoriteView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post,pk=pk)
        if request.user in post.favorite.all():
            post.favorite.remove(request.user)
        else:
            post.favorite.add(request.user)
        return redirect(post.get_absolute_url())
    
class ToggleShareView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post,pk=pk)
        if request.user in post.share.all():
            post.share.remove(request.user)
        else:
            post.share.add(request.user)
        return redirect(post.get_absolute_url())