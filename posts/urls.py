from django.conf.urls import url

from posts.views import PostDetails

urlpatterns = [
    url(r'^(?P<pk>\d+)$', PostDetails.as_view(), name='post_details'),
]