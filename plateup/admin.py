from django.contrib import admin
from .models import Restaurant
from .models import Profile


# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Profile)
