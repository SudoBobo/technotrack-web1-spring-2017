from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)$', BlogDetails.as_view(), name='blog_details'),
]

