from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from posts.models import Post
from comments.models import Comment


class CommentsList(ListView):
    model = Comment

    template_name = 'comments/comments.html'

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post'])
        return Comment.objects.filter(post=post)
