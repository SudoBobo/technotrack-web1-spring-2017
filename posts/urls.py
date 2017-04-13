from django.conf.urls import url

from posts.views import PostDetails, CreatePost

urlpatterns = [
    url(r'^(?P<pk>\d+)$', PostDetails.as_view(), name='post_details'),
    url(r'create_post/$', CreatePost.as_view(), name='create_post')
]
