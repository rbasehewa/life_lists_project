from rest_framework import serializers
from .models import List, Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model.
    - Converts Item model instances to JSON.
    - Validates incoming JSON when creating/updating items.
    """

    class Meta:
        model = Item
        # Fields exposed in the API.
        fields = [
            "id",
            "list",         # References the List (by id).
            "title",
            "description",
            "quantity",
            "is_done",
            "created_at",
        ]
        # These fields are read-only: API will not allow client to set them.
        read_only_fields = ["id", "created_at"]


class ListSerializer(serializers.ModelSerializer):
    """
    Serializer for the List model.

    The 'items' field is nested and read-only:
    - When you GET a list, you will see its items included.
    - When you POST a list, you only send 'name' (no items).
    """

    # items will use the ItemSerializer and return many items.
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = [
            "id",
            "name",
            "created_at",
            "items",   # Nested items of this list.
        ]
        read_only_fields = ["id", "created_at"]
