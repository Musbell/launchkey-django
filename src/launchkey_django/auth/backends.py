"""
launchkey_django.auth.backends
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from django.contrib.auth.backends import ModelBackend
from launchkey_django.models import Association

class AssociationBackend(ModelBackend):
    def authenticate(self, user_hash):
        try:
            association = Association.objects.get(user_hash=user_hash, authorized=True)
        except Association.DoesNotExist:
            return

        return association.user
