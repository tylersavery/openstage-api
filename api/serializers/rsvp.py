from api.models import Rsvp
from rest_framework import serializers
from api.serializers.profile import ProfileSerializer
from api.serializers.stage import StageSerializer

class RsvpSerializer(serializers.HyperlinkedModelSerializer):

    # profile_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    profile = ProfileSerializer(many=False, read_only=True)
    stage = StageSerializer(many=False, read_only=True)

    class Meta:
        model = Rsvp
        fields = ('profile', 'stage')
