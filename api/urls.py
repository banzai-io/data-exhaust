from django.conf.urls import url
from django.urls import include, path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from api.views.internal import banzai
from api.views.external import provider

public_router = DefaultRouter()
public_router.register(r'data-signals', provider.PublicDataSignalViewSet)

public_schema_view = get_schema_view(
   openapi.Info(
      title="Data Exhaust API",
      default_version='v1',
      description="Includes information about the public API endpoints",
   ),
   public=True,
   patterns=[url(r"^api/", include((public_router.urls, "data-signals-doc-public"),))],

)


private_router = DefaultRouter()
private_router.register(r'data-signals-internal', banzai.PrivateDataSignalViewSet, basename='data_signals_internal')


private_schema_view = get_schema_view(
   openapi.Info(
      title="Data Exhaust API - Internal",
      default_version='v1',
      description="Includes information about the private API endpoints",
   ),
   public=True,
   patterns=[url(r"^api/", include((private_router.urls, "data-signals-doc-private"),))],
   permission_classes=(permissions.IsAuthenticated,)
)


router = DefaultRouter()
router.register(r'data-signals-internal', banzai.PrivateDataSignalViewSet, basename='data_signals_internal')
router.register(r'data-signals', provider.PublicDataSignalViewSet)

urlpatterns = [
    url(r'^private/$', private_schema_view.with_ui('redoc', cache_timeout=0), name='schema-private-redoc'),
    url(r'^private-swagger/$', private_schema_view.with_ui('swagger', cache_timeout=0), name='schema-private-swagger'),
    url(r'^public/$', public_schema_view.with_ui('swagger', cache_timeout=0), name='schema-public-swagger'),
    url(r'^documentation/$', public_schema_view.with_ui('redoc', cache_timeout=0), name='schema-public-redoc'),
    path('', include(router.urls)),
]
