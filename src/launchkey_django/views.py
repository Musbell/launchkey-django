"""
launchkey_django.views
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

import json
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404
from launchkey_django.forms import LoginForm
from launchkey_django.models import Association
from launchkey_django.utils import set_auth_request, get_auth_request
from launchkey_django.shortcuts import api
from launchkey_django.constants import (
    POLL_ERROR_NO_REQUEST,
    POLL_ERROR_PENDING_RESPONSE,
    POLL_ERROR_EXPIRED_REQUEST)

try:
    from django.shortcuts import resolve_url
except ImportError:
    resolve_url = lambda x: x

class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'launchkey/login.html'
    success_url = reverse_lazy('launchkey-auth-request')

    def form_valid(self, form):
        set_auth_request(self.request, form.get_auth_request())
        return super(LoginView, self).form_valid(form)

class AuthRequestView(generic.TemplateView):
    template_name = 'launchkey/auth_request.html'

    def auth_request_authorized(self, user_hash):
        user = authenticate(user_hash=user_hash)

        if not user:
            return self.authentication_failed()

        return self.authentication_success(user)

    def auth_request_expired(self):
        messages.error(self.request, _(u"LaunchKey authentication request has expired. Please try again."))
        return HttpResponseRedirect(resolve_url('launchkey-login'))

    def auth_request_check(self, **states):
        return HttpResponse(json.dumps(states), content_type='application/json')

    def authentication_no_request(self):
        return HttpResponseRedirect(resolve_url('launchkey-login'))

    def authentication_failed(self):
        api.logout(get_auth_request(self.request))
        messages.error(self.request, _(u"Could not authenticate with LaunchKey account."))
        return HttpResponseRedirect(resolve_url('launchkey-login'))

    def authentication_success(self, user):
        login(self.request, user)
        return HttpResponseRedirect(resolve_url(settings.LOGIN_REDIRECT_URL))

    def get(self, request, *args, **kwargs):
        auth_request = get_auth_request(request)
        response = api.poll_request(auth_request)
        message_code = response.get('message_code')

        if message_code == POLL_ERROR_NO_REQUEST:
            self.authentication_no_request()

        pending = message_code == POLL_ERROR_PENDING_RESPONSE
        expired = message_code == POLL_ERROR_EXPIRED_REQUEST
        authorized = False

        user_hash = response.get('user_hash')
        auth_package = response.get('auth')

        if auth_package:
            authorized = api.is_authorized(auth_request, auth_package)

        if user_hash:
            if self.request.user and self.request.user.is_authenticated():
                association = Association.objects.associate(self.request.user, user_hash)
            else:
                try:
                    association = Association.objects.get(user_hash=user_hash)
                except Association.DoesNotExist:
                    return self.authentication_failed()

            if authorized:
                association.authorized = authorized
                association.save()

            authorized = association.authorized

        if self.request.is_ajax():
            return self.auth_request_check(
                authorized=authorized,
                pending=pending,
                expired=expired)

        if authorized:
            return self.auth_request_authorized(user_hash)

        if expired:
            return self.auth_request_expired()

        return super(AuthRequestView, self).get(request, *args, **kwargs)

class CallbackView(generic.View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CallbackView, self).dispatch(request, *args, **kwargs)

    def authorize(self, auth_request, user_hash, auth_package):
        association = get_object_or_404(Association, user_hash=user_hash)
        association.authorized = api.is_authorized(auth_request, auth_package)
        association.save()

    def deorbit(self, orbit, signature):
        user_hash = api.deorbit(orbit, signature)
        Association.objects.deauthorize(user_hash)

    def post(self, request, *args, **kwargs):
        auth_request = request.REQUEST.get('auth_request')
        user_hash = request.REQUEST.get('user_hash')
        auth_package = request.REQUEST.get('auth')

        if auth_request and user_hash and auth_package:
            self.authorize(auth_request, user_hash, auth_package)

        deorbit = request.REQUEST.get('deorbit')
        signature = request.REQUEST.get('signature')

        if deorbit and signature:
            self.deorbit(deorbit, signature)

        return HttpResponse()
