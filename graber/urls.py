from django.conf.urls import patterns, url

from graber import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^query\/?(\w*)', views.query, name='query'),
    url(r'\/update$', views.update, name='update'),
)
