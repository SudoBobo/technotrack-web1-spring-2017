from django.shortcuts import render, resolve_url
from django.views.generic import CreateView
from django.views.generic import UpdateView

from django.views.generic import DetailView
from django.views.generic import ListView

from blogs.models import Blog

from django.contrib.auth.mixins import LoginRequiredMixin
from blogs.forms import CreateBlogForm, UpdateBlogForm

from fm.views import AjaxCreateView, AjaxUpdateView

from blogs.forms import CreateBlogForm
from blogs.forms import UpdateBlogForm


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


class CreateBlog(LoginRequiredMixin, AjaxCreateView):
    form_class = CreateBlogForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateBlog, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('blogs:blog_details', pk=self.object.pk)


class UpdateBlog(LoginRequiredMixin, AjaxUpdateView):
    form_class = UpdateBlogForm

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return resolve_url('blogs:blog_details', pk=self.object.pk)
