from django.conf.urls import url
from django.urls import include, path
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions
from api.views.internal import banzai
from api.views.external import provider


schema_view = get_schema_view(
   openapi.Info(
      title="Data Exhaust API",
      default_version='v1',
      description="Includes information about the public and private API endpoints",
   ),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)


router = DefaultRouter()
router.register(r'data-signals-internal', banzai.PrivateDataSignalViewSet)
router.register(r'data-signals', provider.PublicDataSignalViewSet)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
