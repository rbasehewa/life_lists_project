from django.contrib import admin
from .models import List, Item


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    """
    This class customises how the List model appears in the Django admin site.
    """
    # Columns to show in the admin list view.
    list_display = ("id", "name", "user", "created_at")

    # Search box will search by name.
    search_fields = ("name",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Item model.
    """
    # Columns in the list view.
    list_display = ("id", "title", "list", "quantity", "is_done", "created_at")

    # Filters on the right side of the admin page.
    list_filter = ("is_done", "list")

    # Search box fields.
    search_fields = ("title",)
