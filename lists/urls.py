from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListViewSet, ItemViewSet

# Router automatically creates routes for our ViewSets.
router = DefaultRouter()

# Register URL prefixes and link them to viewsets.
# /api/lists/ will go to ListViewSet
router.register(r"lists", ListViewSet)

# /api/items/ will go to ItemViewSet
router.register(r"items", ItemViewSet)

# Expose all the router-generated URLs.
urlpatterns = [
    path("", include(router.urls)),
]
