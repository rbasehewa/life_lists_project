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
├── manage.py             # Django management script
├── db.sqlite3            # Dev database (ignored in git)
├── venv/                 # Virtual environment (ignored in git)
└── README.md             # This file
