from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'purge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^user_login/$', views.user_login),
    url(r'^logout/$', views.logout),
    url(r'^forgot/$', views.forgot),
    url(r'^purge/(\d)+/$', views.purgesite),
)
