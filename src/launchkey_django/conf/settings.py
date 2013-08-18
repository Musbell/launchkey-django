"""
launchkey_django.conf.settings
------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from django.conf import settings

LAUNCHKEY_APP_KEY = getattr(settings, 'LAUNCHKEY_APP_KEY', None)
LAUNCHKEY_SECRET_KEY = getattr(settings, 'LAUNCHKEY_SECRET_KEY', None)
LAUNCHKEY_PRIVATE_KEY = getattr(settings, 'LAUNCHKEY_PRIVATE_KEY', None)
