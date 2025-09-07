# CodeLeap Backend Challenge (Django)

A minimal CRUD API for posts.

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
Base URL: `http://localhost:8000/`

- Create post: `POST /`
  - Body: `{ "username": "string", "title": "string", "content": "string" }`
  - Response: `201` with created object

- List posts: `GET /`
  - Response: array of posts
  - Fields: `{ "id": number, "username": string, "created_datetime": datetime, "title": string, "content": string }`

- Update post: `PATCH /{id}/`
  - Body: `{ "title": "string", "content": "string" }`
  - Cannot change `id`, `username`, or `created_datetime` as the challenge states
  - Response: only `{ "title": string, "content": string }`

- Delete post: `DELETE /{id}/`
  - Response: `204` No Content

## Examples
```bash
# Create
curl -s -X POST http://localhost:8000/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","title":"Hello","content":"First post"}'

# List
curl -s http://localhost:8000/

# Update (only title and content are returned)
curl -s -X PATCH http://localhost:8000/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"New title","content":"Updated"}'

# Delete
curl -s -X DELETE http://localhost:8000/1/
```

## Environment variables
The app supports a few simple environment variables (all optional FOR DEVELOPMENT):

- `DJANGO_SECRET_KEY`: Secret key for Django. Default: `dev-secret-key-change-me`.
- `DJANGO_DEBUG`: Enable debug mode (`1` or `0`). Default: `1`.
- `DJANGO_ALLOWED_HOSTS`: Comma-separated allowed hosts. Default: `*`.