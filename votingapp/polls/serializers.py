from .models import User, UserProfile, Candidate, Event
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'        

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'