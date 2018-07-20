from api.models import Stage
from rest_framework import serializers

class StageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stage
        fields = ('kind', 'day_of_week', 'start_time', 'end_time', 'venue_name')
