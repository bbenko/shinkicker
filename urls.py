from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler500 = 'djangotoolbox.errorviews.server_error'
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls')),
)


if settings.SERVE_MEDIA:
    urlpatterns += staticfiles_urlpatterns()
