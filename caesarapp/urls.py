from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^encrypt/$', views.encrypt, name='encrypt'),
    url(r'^(?P<raw_message>[a-z]*)/encrypted/$', views.encrypted, name='encrypted'),
]
