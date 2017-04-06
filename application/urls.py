"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin

import blogs
from core.views import HomePageView

from django.conf.urls import include, url

from registration.backends.simple.views import RegistrationView

from application.form import MyRegistrationForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # передаёт URL в blogs.url без "blogs/"?

    # Whenever Django encounters include() (django.conf.urls.include()), it chops off whatever part of
    # the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

    # Почему не делаем так?
    # url(r'blogs/', blogs.urls) - нет чопа
    # как внизу - есть

    url(r'^blogs/', include('blogs.urls', namespace="blogs")),
    url(r'^core/', include('core.urls', namespace="core")),
    url(r'^posts/', include('posts.urls', namespace="posts")),
    url(r'^comments/', include('comments.urls', namespace="comments")),
    url(r'^$', HomePageView.as_view(), name="home"),
    # url(r'^accounts/', include('registration.backends.simple.urls'), name="registration"),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=MyRegistrationForm),name='registration'),
]


#
# urlpatterns = [
#     # ... other URL patterns here
#     url(r'^accounts/register/$',
#         RegistrationView.as_view(
#             form_class=MyCustomUserForm
#         ),
#         name='registration_register',
#     ),
#     url(r'^accounts/', include('registration.backends.hmac.urls')),
# ]
