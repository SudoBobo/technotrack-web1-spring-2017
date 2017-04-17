from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, resolve_url, get_object_or_404
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from fm.views import AjaxUpdateView, AjaxCreateView

from posts.forms import CreatePostForm, UpdatePostForm, CreateCommentForm

from posts.models import Post


class PostDetails(CreateView):
    form_class = CreateCommentForm
    template_name = 'posts/post_details.html'

    postobject = None

    # ?
    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied()
        return super().post(request, *args, **kwargs)

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDetails, self).dispatch(request, *args, **kwargs)

    # Это контекст для html-ки
    def get_context_data(self, **kwargs):
        context = super(PostDetails, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context

    # Это то, что отправляется на сервер
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postobject
        return super(PostDetails, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('posts:post_details', pk=self.postobject.id)


class CreatePost(LoginRequiredMixin, AjaxCreateView):
    form_class = CreatePostForm

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return resolve_url('posts:post_details', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, AjaxUpdateView):
    form_class = UpdatePostForm

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('posts:post_details', pk=self.object.pk)
