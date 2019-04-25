from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'bookticket/(?P<id>[0-9])/$', views.BookingAction.as_view(),name='bookticket'),
]
