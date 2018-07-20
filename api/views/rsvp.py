from api.models import Rsvp
from rest_framework import viewsets
from api.serializers.rsvp import RsvpSerializer

class RsvpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rsvps to be viewed or edited.
    """
    queryset = Rsvp.objects.all()
    serializer_class = RsvpSerializer

