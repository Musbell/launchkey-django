"""
launchkey_django.admin
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from django.contrib import admin
from launchkey_django.models import Association

admin.site.register(Association)
