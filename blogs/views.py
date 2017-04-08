from django.shortcuts import render, resolve_url
from django.views.generic import CreateView
from django.views.generic import UpdateView

from django.views.generic import DetailView
from django.views.generic import ListView

from blogs.models import Blog

from django.contrib.auth.mixins import LoginRequiredMixin
from blogs.forms import CreateBlogForm, UpdateBlogForm


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


class CreateBlog(LoginRequiredMixin, CreateView):
    form_class = CreateBlogForm
    template_name = 'blogs/create_blog.html'

    def get_success_url(self):
        return resolve_url('blogs:blog_details', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateBlog, self).form_valid(form)


class UpdateBlog(LoginRequiredMixin, UpdateView):
    template_name = 'blogs/update_blog_new.html'
    form_class = UpdateBlogForm

    def get_success_url(self):
        return resolve_url('blogs:blog_details', pk=self.object.pk)

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user)
