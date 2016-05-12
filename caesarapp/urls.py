from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^encrypt/$', views.encrypt, name='encrypt'),
    url(r'^(?P<userInput_id>[0-9]+)/encrypted/$', views.encrypted, name='encrypted'),
]
