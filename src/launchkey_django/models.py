"""
launchkey_django.models
-------------------

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""

from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class AssociationManager(models.Manager):
    def associate(self, user, user_hash):
        association, created = self.get_or_create(user=user, defaults={
            'user_hash': user_hash
        })

        if not created:
            association.user_hash = user_hash
            association.save()

        return association

    def authorize(self, user_hash):
        try:
            association = self.get_query_set().get(user_hash=user_hash)
            association.authorize()
            association.authorized = True
            association.save()
        except self.model.DoesNotExist:
            pass

    def deauthorize(self, user_hash):
        try:
            association = self.get_query_set().get(user_hash=user_hash)
            association.authorized = False
            association.save()
        except self.model.DoesNotExist:
            pass

class Association(models.Model):
    user_hash = models.CharField(max_length=64, primary_key=True)
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='launchkey_association')
    authorized = models.BooleanField()

    objects = AssociationManager()

    def __unicode__(self):
        return u"%s -> %s" % (self.user_hash, unicode(self.user))

from launchkey_django.receivers import *
