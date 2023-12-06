from django.contrib.auth.models import User
from .models import ToDoUserProfile
from rest_framework import serializers

class ToDoUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoUserProfile
        fields = ('pseudo', 'email', 'password')
        
class UserSerializer(serializers.ModelSerializer):
    profile = ToDoUserProfileSerializer(source='todouserprofile')
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'profile')