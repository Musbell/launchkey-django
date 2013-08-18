"""
launchkey_django.receivers
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out
from launchkey_django.shortcuts import api
from launchkey_django.utils import get_auth_request

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    auth_request = get_auth_request(request)
    api.logout(auth_request)
