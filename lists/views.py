from rest_framework import viewsets
from .models import List, Item
from .serializers import ListSerializer, ItemSerializer


class ListViewSet(viewsets.ModelViewSet):
    """
    ViewSet for List model.

    ModelViewSet provides built-in actions:
    - list    -> GET /api/lists/
    - create  -> POST /api/lists/
    - retrieve-> GET /api/lists/{id}/
    - update  -> PUT /api/lists/{id}/
    - partial_update -> PATCH /api/lists/{id}/
    - destroy -> DELETE /api/lists/{id}/
    """

    # Which objects this viewset works with.
    queryset = List.objects.all().order_by("-created_at")

    # Which serializer to use to convert List <-> JSON.
    serializer_class = ListSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Item model.

    Endpoints:
    - GET /api/items/
    - POST /api/items/
    - GET /api/items/{id}/
    - PUT /api/items/{id}/
    - PATCH /api/items/{id}/
    - DELETE /api/items/{id}/
    """

    queryset = Item.objects.all().order_by("-created_at")
    serializer_class = ItemSerializer
