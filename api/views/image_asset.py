from api.models import ImageAsset
from rest_framework import viewsets
from api.serializers.image_asset import ImageAssetSerializer

class ImageAssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows image assets to be viewed or edited.
    """
    queryset = ImageAsset.objects.all()
    serializer_class = ImageAssetSerializer

