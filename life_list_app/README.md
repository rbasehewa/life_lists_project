# Life Lists API

A simple Django + Django REST Framework backend for a **"life lists"** app.

The idea is to have one place to track all the little things you remember during the day:
- Shopping list (e.g. salt, milk, coffee)
- School / study list (e.g. new notebook, assignment reminders)
- Office / work list (e.g. printer ink, TODOs)
- Home tasks

This project will be used later by an Android app as the mobile frontend.

---

## Tech Stack

- **Python** (3.14)
- **Django**
- **Django REST Framework**
- **SQLite**

---

## Project Structure

```text
life_lists_project/
├── life_list_app/        # Main Django project (settings, urls, etc.)
├── lists/                # App containing List and Item models + API
│   ├── models.py         # List and Item database models
│   ├── serializers.py    # Converts models to/from JSON
│   ├── views.py          # API ViewSets (handles requests)
│   ├── urls.py           # URL routing via DefaultRouter
│   └── admin.py          # Admin panel registration
├── manage.py             # Django management script
├── db.sqlite3            # Dev database (ignored in git)
├── venv/                 # Virtual environment (ignored in git)
└── README.md             # This file
```

---

## Getting Started

### 1. Clone the repo and navigate into it

```bash
git clone <your-repo-url>
cd life_lists_project
```

### 2. Create and activate virtual environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\Activate.ps1

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000`

---

## Admin Panel

```
http://127.0.0.1:8000/admin/
```

| Field    | Value       |
|----------|-------------|
| Username | yes         |
| Password | Testing123! |

---

## Data Models

### List (`models.py`)

```python
class List(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    name       = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Item (`models.py`)

```python
class Item(models.Model):
    list        = models.ForeignKey(List, on_delete=models.CASCADE, related_name="items")
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity    = models.PositiveIntegerField(default=1)
    is_done     = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
```

---

## Serializers

### ItemSerializer

```python
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Item
        fields = ["id", "list", "title", "description", "quantity", "is_done", "created_at"]
        read_only_fields = ["id", "created_at"]
```

### ListSerializer (nested)

```python
class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)  # nested items

    class Meta:
        model  = List
        fields = ["id", "name", "created_at", "items"]
        read_only_fields = ["id", "created_at"]
```

---

## Views

```python
class ListViewSet(viewsets.ModelViewSet):
    queryset         = List.objects.all().order_by("-created_at")
    serializer_class = ListSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset         = Item.objects.all().order_by("-created_at")
    serializer_class = ItemSerializer
```

`ModelViewSet` automatically provides:

| Action         | Method | URL              |
|----------------|--------|------------------|
| list           | GET    | /api/lists/      |
| create         | POST   | /api/lists/      |
| retrieve       | GET    | /api/lists/{id}/ |
| update         | PUT    | /api/lists/{id}/ |
| partial_update | PATCH  | /api/lists/{id}/ |
| destroy        | DELETE | /api/lists/{id}/ |

---

## URL Routing

```python
router = DefaultRouter()
router.register(r"lists", ListViewSet)
router.register(r"items", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
```

---

## API Endpoints

Base URL: `http://127.0.0.1:8000/api/`

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| GET    | /api/lists/      | Get all lists       |
| POST   | /api/lists/      | Create a new list   |
| GET    | /api/lists/{id}/ | Get a specific list |
| PUT    | /api/lists/{id}/ | Update a list       |
| DELETE | /api/lists/{id}/ | Delete a list       |
| GET    | /api/items/      | Get all items       |
| POST   | /api/items/      | Create a new item   |
| GET    | /api/items/{id}/ | Get a specific item |
| PUT    | /api/items/{id}/ | Update an item      |
| DELETE | /api/items/{id}/ | Delete an item      |

---

## Example API Usage

### Create a List

```http
POST /api/lists/
Content-Type: application/json

{
  "name": "Shopping"
}
```

```json
{
  "id": 1,
  "name": "Shopping",
  "created_at": "2025-02-24T10:00:00Z",
  "items": []
}
```

---

### Get All Lists (with nested items)

```http
GET /api/lists/
```

```json
[
  {
    "id": 1,
    "name": "Shopping",
    "created_at": "2025-02-24T10:00:00Z",
    "items": [
      {
        "id": 1,
        "list": 1,
        "title": "Buy milk",
        "description": "Full cream, 2L",
        "quantity": 2,
        "is_done": false,
        "created_at": "2025-02-24T10:05:00Z"
      }
    ]
  }
]
```

---

### Create an Item

```http
POST /api/items/
Content-Type: application/json

{
  "list": 1,
  "title": "Buy milk",
  "description": "Full cream, 2L",
  "quantity": 2,
  "is_done": false
}
```

```json
{
  "id": 1,
  "list": 1,
  "title": "Buy milk",
  "description": "Full cream, 2L",
  "quantity": 2,
  "is_done": false,
  "created_at": "2025-02-24T10:05:00Z"
}
```

---

### Mark an Item as Done

```http
PATCH /api/items/1/
Content-Type: application/json

{
  "is_done": true
}
```

```json
{
  "id": 1,
  "list": 1,
  "title": "Buy milk",
  "description": "Full cream, 2L",
  "quantity": 2,
  "is_done": true,
  "created_at": "2025-02-24T10:05:00Z"
}
```

---

### Delete a List

```http
DELETE /api/lists/1/
```

```
204 No Content
```

---

## How the Files Connect

```
Client Request
     │
     ▼
urls.py          → DefaultRouter matches /api/lists/ → ListViewSet
     │
     ▼
views.py         → ModelViewSet handles GET/POST/PUT/PATCH/DELETE
     │
     ▼
serializers.py   → Validates data, converts Model ↔ JSON
     │              ListSerializer nests ItemSerializer
     ▼
models.py        → ORM queries the database
     │
     ▼
db.sqlite3       → Data stored/retrieved
```

---

## Notes

- `PATCH` updates a single field. `PUT` replaces the whole object.
- Deleting a List also deletes all its Items (`on_delete=models.CASCADE`).
- The `items` field in ListSerializer is read-only — you cannot POST items via `/api/lists/`, use `/api/items/` instead.
- For production, replace SQLite with PostgreSQL in `settings.py`.
- `db.sqlite3` and `venv/` should be in `.gitignore`.