from django.urls import include, path
from rest_framework.routers import DefaultRouter
from signal_data import views

router = DefaultRouter()
router.register(r'data-signals', views.DataSignalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]