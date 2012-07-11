from django.conf.urls.defaults import patterns, url
from models import Post
from django.views.generic import ListView
from views import PostDetailView
from models import PUBLISHED

urlpatterns = patterns('',
                       url(r'^$', ListView.as_view(queryset=Post.objects.filter(status=PUBLISHED)[:3]), name="home"),
                       url(r'^$', ListView.as_view(queryset=Post.objects.filter(status=PUBLISHED)[3:]), name="archive"),
                       url(r'^(?P<pk>\d+)$', PostDetailView.as_view(model=Post), name="post"),
)
