from .models import User
from rest_framework import serializers


class UserSerializaer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'