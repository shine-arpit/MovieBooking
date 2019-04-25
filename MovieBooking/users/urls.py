from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'users/registration/login.html'}, name='login'),
]
