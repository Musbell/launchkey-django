"""
launchkey_django.forms
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from django import forms
from django.utils.translation import ugettext as _
from launchkey_django.shortcuts import api

AUTHORIZE_ERROR_RESPONSE = 'Error'

class LoginForm(forms.Form):
    username = forms.CharField()

    def clean_username(self):
        auth_request = api.authorize(self.cleaned_data['username'])

        if auth_request == AUTHORIZE_ERROR_RESPONSE:
            raise forms.ValidationError(_(u"Could not login to LaunchKey"))

        self._auth_request = auth_request

    def get_auth_request(self):
        return self._auth_request
