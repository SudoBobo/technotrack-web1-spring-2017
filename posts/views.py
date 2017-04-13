from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, resolve_url
from django.views.generic import CreateView
from django.views.generic import DetailView

from posts.forms import CreatePostForm

from posts.models import Post


class PostDetails(DetailView):
    template_name = 'posts/post_details.html'
    model = Post


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'posts/create_post.html'

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return resolve_url('posts:post_details', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)
