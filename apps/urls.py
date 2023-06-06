from django.urls import path, include
from apps.views import ProductModelViewSet, CategoryModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', ProductModelViewSet)
router.register(r'api2', CategoryModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]