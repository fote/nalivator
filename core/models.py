from __future__ import unicode_literals
from django.db import models


class Beverage(models.Model):
    name = models.CharField(max_length=128, default='', blank=False, unique=True)
    alc = models.PositiveSmallIntegerField(blank=True)
    density = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    name = models.CharField(max_length=128, default='', blank=False, unique=True)
    ing1 = models.ForeignKey(Beverage, related_name='ing1')
    ing2 = models.ForeignKey(Beverage, related_name='ing2', blank=True, null=True)
    ing3 = models.ForeignKey(Beverage, related_name='ing3', blank=True, null=True)

    ing1_p = models.PositiveSmallIntegerField(null=True, blank=True)
    ing2_p = models.PositiveSmallIntegerField(null=True, blank=True)
    ing3_p = models.PositiveSmallIntegerField(null=True, blank=True)

    in_work = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.in_work:
            try:
                temp = Cocktail.objects.get(in_work=True)
                if self != temp:
                    temp.in_work = False
                    temp.save()
            except Cocktail.DoesNotExist:
                pass
        super(Cocktail, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class CurrentCoctailSet(models.Model):
    cocktail_in_set = models.ForeignKey(Cocktail)

    def __str__(self):
        return self.cocktail_in_set.name

class CurrentPumpSet(models.Model):
    pump1 = models.ForeignKey(Beverage, related_name='pump1', blank=True, null=True)
    pump2 = models.ForeignKey(Beverage, related_name='pump2', blank=True, null=True)
    pump3 = models.ForeignKey(Beverage, related_name='pump3', blank=True, null=True)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = CurrentPumpSet.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except CurrentPumpSet.DoesNotExist:
                pass
        super(CurrentPumpSet, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.pump1) + '.' + str(self.pump2) + '.' + str(self.pump3)
