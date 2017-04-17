from django.shortcuts import render, resolve_url
from django.views.generic import CreateView
from django.views.generic import UpdateView

from django.views.generic import DetailView
from django.views.generic import ListView

from blogs.models import Blog

from django.contrib.auth.mixins import LoginRequiredMixin
from blogs.forms import CreateBlogForm, UpdateBlogForm, FilterForm

from fm.views import AjaxCreateView, AjaxUpdateView

from blogs.forms import CreateBlogForm
from blogs.forms import UpdateBlogForm


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog
    filter_form = None

    def dispatch(self, request, *args, **kwargs):
        self.filter_form = FilterForm(request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        return context

    def get_queryset(self):
        qs = Blog.objects.all()
        if self.filter_form.is_valid():
            if self.filter_form.cleaned_data.get('sort'):
                qs = qs.order_by(self.filter_form.cleaned_data['sort'])
            qs = qs.filter(title__contains=self.filter_form.cleaned_data['search'])
        return qs


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
