from django.shortcuts import render
from django.views.generic import DetailView

from posts.models import Post


class PostDetails(DetailView):
    template_name = 'posts/post_details.html'
    model = Post

