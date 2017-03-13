from django.shortcuts import render

from django.views.generic.base import TemplateView

from blogs.models import Blog
from posts.models import Post
from comments.models import Comment

class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['n_blogs'] = Blog.objects.all().count();
        context['n_posts'] = Post.objects.all().count();
        context['n_comments'] = Comment.objects.all().count();
        return context
