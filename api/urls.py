from django.conf.urls import url, include
from rest_framework import routers
from api.views import user


router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]