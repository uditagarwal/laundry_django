# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255, null=True)
    firstName = models.CharField(max_length=70, null=True)
    lastName = models.CharField(max_length=70, null=True)
    USER_TYPES = (
        ('D', 'Dirty'),
        ('W', 'Washr')
    )
    type = models.CharField(max_length=1, choices=USER_TYPES, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class Addresses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    zipCode = models.TextField(null=True)
    locationName = models.CharField(max_length=50, null=True)

class PaymentAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
