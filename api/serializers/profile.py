from api.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = ('user_id', 'is_performer', 'is_host', 'bio', 'city', 'avatar_url', 'created_at')
