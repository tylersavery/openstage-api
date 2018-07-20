from api.models import ImageAsset
from rest_framework import serializers

class ImageAssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageAsset
        fields = ('url', 'width', 'height')
