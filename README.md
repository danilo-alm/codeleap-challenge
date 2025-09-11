# CodeLeap Backend Challenge (Django)

A minimal CRUD API for posts.

Note: The base of the challenge was implemented before sending the form, however the Reactions feature was implemented after it.

## Tech
- Django 5, Django REST Framework
- uv for dependency management
- SQLite for storage

## Setup
```bash
# Install deps
uv sync

# Apply migrations
uv run python manage.py migrate

# Run dev server
uv run python manage.py runserver 0.0.0.0:8000  # or whatever port you like
```

## Endpoints

You can test the API manually by importing [this file](./postman_collection.json) into postman, insomnia or your preferred software.

## Environment variables
The app supports a few simple environment variables (all optional FOR DEVELOPMENT):

- `DJANGO_SECRET_KEY`: Secret key for Django. Default: `dev-secret-key-change-me`.
- `DJANGO_DEBUG`: Enable debug mode (`1` or `0`). Default: `1`.
- `DJANGO_ALLOWED_HOSTS`: Comma-separated allowed hosts. Default: `*`.