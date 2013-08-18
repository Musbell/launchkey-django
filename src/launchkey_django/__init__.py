"""
launchkey_django
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

try:
    VERSION = __import__('pkg_resources').get_distribution('launchkey').version
except Exception, e:
    VERSION = 'unknown'
