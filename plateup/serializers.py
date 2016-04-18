from rest_framework import serializers
from plateup.models import Restaurant,STARS
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model=User
        fields=('id', 'name','sex','restaurant')

class RestaurantSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model=Restaurant
        fields=('id', 'name', 'cuisine','rating','users')

