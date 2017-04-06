from django.shortcuts import render

from django.views.generic import DetailView
from django.views.generic import ListView

from blogs.models import Blog


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog



    # def get_queryset(self):
    #     sorting = self.request.Get('sort', 'title')
    #     if sorting not in ('title', 'rate', 'desctiption'):
    #         qs = super(BlogList, self).get_queryset()
    #     qs = qs.order_by(sorting)
    #     return qs


class BlogDetails(DetailView):
    template_name = 'blogs/blog_details.html'
    model = Blog
