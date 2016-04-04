from __future__ import unicode_literals

from django.db import models

STARS = ((1, 'one'),
         (2, 'two'),
         (3, 'three'),
         (4, 'four'),
         (5, 'five'))
GENDER = (('M', 'male'),
          ('F', 'female'),
          ('N/A', 'not defined'))

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=30)
    cuisine=models.CharField(max_length=20)
    rating=models.IntegerField(choices=STARS, default=1)
    picture = models.ImageField(upload_to='images/', null=True)

    def __unicode__(self):
        return self.name


class User(models.Model):
    name=models.CharField(max_length=30)
    sex=models.CharField(choices=GENDER, default='not defined', max_length=15)
    age=models.IntegerField(blank=True, default=0)
    restaurant=models.ManyToManyField(Restaurant, related_name='users')

    def __unicode__(self):
        return self.name







