"""
launchkey_django.conf.urls
------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django < 1.5
    from django.conf.urls.defaults import patterns, url

from launchkey_django import views as auth

urlpatterns = patterns('', 
    url(r'^login/$', auth.LoginView.as_view(), name='launchkey-login'),
    url(r'^authenticating/$', auth.AuthRequestView.as_view(), name='launchkey-auth-request'),
    url(r'^callback/$', auth.CallbackView.as_view(), name='launchkey-callback'),
)
