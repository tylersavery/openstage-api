from django.conf.urls import url, include
from rest_framework import routers
from api.views import user, stage, image_asset, rsvp


router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet)
router.register(r'stages', stage.StageViewSet)
router.register(r'images', image_asset.ImageAssetViewSet)
router.register(r'rsvps', rsvp.RsvpViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]