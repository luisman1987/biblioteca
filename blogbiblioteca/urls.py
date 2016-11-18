from django.conf.urls import include, url
from blogbiblioteca import views

urlpatterns = [
    url(r'^$', 'blogbiblioteca.views.post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'blogbiblioteca.views.post_detail'),
    url(r'^post/new/$', 'blogbiblioteca.views.post_new', name='post_new'),
]
