"""
launchkey_django.middleware
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist

class DeorbitMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return

        try:
            association = request.user.launchkey_association
        except ObjectDoesNotExist:
            association = None

        if association and not association.authorized:
           logout(request)
