from django.conf.urls import patterns, url

from light_cms import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^page/(?P<article_slug>[\w-]+)/$', views.PageView.as_view(), name='page'),
)
