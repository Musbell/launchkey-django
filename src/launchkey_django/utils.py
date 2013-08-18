"""
launchkey_django.utils
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from launchkey_django.constants import AUTH_REQUEST_SESSION_KEY

def set_auth_request(request, auth_request):
    request.session[AUTH_REQUEST_SESSION_KEY] = auth_request

def get_auth_request(request):
    return request.session.get(AUTH_REQUEST_SESSION_KEY)
