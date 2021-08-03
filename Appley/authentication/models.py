from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(models.Model):
    username=models.CharField(_("Username"), max_length=100, null=True, blank=False)
    email=models.CharField(_("Email"), max_length=100, null=True, blank=False)
    password=models.CharField(_("Password"), max_length=100, null=True, blank=False)

    def __str__(self):
        return '%s %s %s' % (self.email, self.username) 

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
