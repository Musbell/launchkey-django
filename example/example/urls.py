from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^orbit/$', login_required(TemplateView.as_view(template_name='orbit.html')), name='orbit'),
    url(r'^launchkey/', include('launchkey_django.conf.urls')),
)
