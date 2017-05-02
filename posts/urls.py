from django.conf.urls import url

from posts.views import PostDetails, CreatePost, UpdatePost, PostLikeAjaxView, PostCommentsView

urlpatterns = [
    url(r'^(?P<pk>\d+)$', PostDetails.as_view(), name='post_details'),
    url(r'create_post/$', CreatePost.as_view(), name='create_post'),
    url(r'update_post/(?P<pk>\d+)', UpdatePost.as_view(), name='update_post'),
    url(r'ajax_like/(?P<pk>\d+)', PostLikeAjaxView.as_view(), name='post_ajax_like'),
    url(r'(?P<pk>\d+)/comments/$', PostCommentsView.as_view(), name='post_comments'),
]
