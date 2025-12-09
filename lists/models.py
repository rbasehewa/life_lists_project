from django.conf import settings
from django.db import models


class List(models.Model):
    """
    Represents a logical list, like:
    - Shopping
    - School
    - Office
    - Home

    Each list can belong to a user (optional for now).
    """

    # Link to the Django User model.
    # null=True, blank=True allows us to skip setting a user while we are learning.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lists",
        null=True,
        blank=True,
    )

    # Name of the list (Shopping, Work, etc.)
    name = models.CharField(max_length=100)

    # Automatically stores the time when the list was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        This is what Django shows in the admin / shell.
        Returning the name makes it easier to read.
        """
        return self.name


class Item(models.Model):
    """
    Represents a single item inside a list, like:
    - "Salt" in Shopping
    - "Maths book" in School list
    """

    # Each item belongs to one List (parent).
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,   # If the list is deleted, delete its items too.
        related_name="items",       # Allows list.items.all() to get all items.
    )

    # Short title of the item.
    title = models.CharField(max_length=255)

    # Optional description (can be empty).
    description = models.TextField(blank=True)

    # Quantity of the item (defaults to 1).
    quantity = models.PositiveIntegerField(default=1)

    # Checkbox: is this item completed / bought / done?
    is_done = models.BooleanField(default=False)

    # When the item was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        This appears in the admin and Django shell.
        Shows title + quantity for readability.
        """
        return f"{self.title} (x{self.quantity})"
