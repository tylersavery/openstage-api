from api.models import Stage
from rest_framework import viewsets
from api.serializers.stage import StageSerializer

class StageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stages to be viewed or edited.
    """
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

