from django.views.generic import (ListView,
                                  DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import *
# Create your views here.


class HomePageView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    ordering = ['-pub_date']
    paginate_by = 5

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return User.objects.filter(username=user).order_by('-pub_date')


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = ['title', 'body']
    login_url = 'login'

    def post(self, request, pk, *args, **kwargs):
        post = Blog.objects.get(pk=pk)
        if post.author != self.request.user:
            raise PermissionDenied
        return super().post(request, *args, **kwargs)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
    login_url = 'login'

    def post(self, request, pk, *args, **kwargs):
        post = Blog.objects.get(pk=pk)
        if post.author != self.request.user:
            raise PermissionDenied
        return super().post(request, *args, **kwargs)
