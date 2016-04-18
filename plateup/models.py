from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save, class_prepared

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


    def __unicode__(self):
        return self.name


class Profile(models.Model):
    owner=models.ForeignKey('auth.User', related_name='Profile')
    sex=models.CharField(choices=GENDER, default='not defined', max_length=15)
    age=models.IntegerField(blank=True, default=0)
    restaurant=models.ManyToManyField(Restaurant, related_name='users', blank=True)

    def __unicode__(self):
        return unicode(self.owner)

def create_user_Info(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_create(owner=instance)

post_save.connect(create_user_Info, sender=User)








