from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views.internal import banzai
from api.views.external import provider


router = DefaultRouter()
router.register(r'data-signals-internal', banzai.PrivateDataSignalViewSet)
router.register(r'data-signals', provider.PublicDataSignalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
