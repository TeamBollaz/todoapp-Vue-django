from django.db import models
from django.utils.translation import ugettext_lazy as _

class Fruit(models.Model):
    fruitname=models.CharField(_("Fruitname"), max_length=100)
    ftype=models.CharField(_("Fruit Type"), max_length=100)
    region=models.CharField(_("Where Found"), max_length=100,  null=True)

    def __str__(self):
        return self.fruitname 

    class Meta:
        verbose_name='Fruit'
        verbose_name_plural='Fruits'

