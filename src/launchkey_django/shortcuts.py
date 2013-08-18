"""
launchkey_django.shortcuts
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

import launchkey
from launchkey_django.conf import settings

api = launchkey.API(
    settings.LAUNCHKEY_APP_KEY,
    settings.LAUNCHKEY_SECRET_KEY,
    settings.LAUNCHKEY_PRIVATE_KEY)
