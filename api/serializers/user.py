from django.contrib.auth.models import User
from api.serializers.profile import ProfileSerializer
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    profile = ProfileSerializer(many=False, read_only=True)
    
    class Meta:
        model = User
        fields = ('url', 'profile', 'username', 'email', 'groups')
