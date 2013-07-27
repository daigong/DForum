# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
from registration.views import register
from lbforum.accountviews import profile
import api_views

admin.autodiscover()

urlpatterns = patterns(  # (r'^accounts/avatar/', include('simpleavatar.urls')),
                         # Examples:
                         # url(r'^$', 'bbs.views.home', name='home'),
                         # url(r'^bbs/', include('bbs.foo.urls')),
                         # Uncomment the admin/doc line below to enable admin documentation:
                         # Uncomment the next line to enable the admin:
                         # 后台插入接口
    '',
    url(r'^accounts/register/$', register,
        {'backend': 'lbregistration.backends.simple.SimpleBackend'},
        name='registration_register'),
    url(r'^user/(?P<user_id>\d+)/$', profile, name='user_profile'),
    url(r'^captcha/', include('captcha.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^attachments/', include('attachments.urls')),
    (r'^', include('lbforum.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/new/(?P<forum_id>\d+)/$', api_views.new_post),
    )
