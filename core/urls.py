import registration
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.conf.urls import include

urlpatterns = [
    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),
    # url(r'^register/', 'registration.simple.views.RegistrationView'),
]
