from .models import *
from rest_framework import serializers
from django.conf import settings


#Registration Serializer
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user