from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateFileViewSet, ListFileViewSet

router = DefaultRouter()

router.register('upload', CreateFileViewSet)
router.register('files', ListFileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
