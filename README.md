# VRMS API

---

# Development

## Requirements

- Docker
- Python 3.13+ (only for local LSP support, not required to run the app)

---

## Running the App (Docker)

Build the image:

```bash
docker build -t vrms-image .
```

Run the container with live reload:

```bash
docker run --rm -p <host_port>:8000 -v $(pwd):/app vrms-image
```

The API will be available at `http://localhost:3004`.

> Only rebuild the image when you change `requirements.txt`. For code changes, the volume mount handles live reload automatically.

---

## Migrations

Migrations are how Django manages your database schema. When you change your models, you need to run two commands:

**Generate the migration file** (does not touch the database, just creates the file):

```bash
docker run --rm -v $(pwd):/app vrms-image python manage.py makemigrations
```

**Apply the migrations to the database** (actually creates/updates the tables):

```bash
docker run --rm -v $(pwd):/app vrms-image python manage.py migrate
```

> Always run `makemigrations` before `migrate`. Every time you add, remove, or change a field in `models.py`, you need to run both commands.

---

## LSP Setup (Neovim / Pyright)

This is only needed for editor support (autocomplete, type checking). The app itself runs entirely in Docker.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

Deactivate when done:

```bash
deactivate
```

Make sure your `pyrightconfig.json` has:

```json
{
  "venvPath": ".",
  "venv": "venv"
}
```

---

# Production
 
## Requirements
 
- Docker or Podman
- Nginx running on the host
- MySQL running on the host
 
---
 
## Build the Image
 
```bash
docker build -t vrms-image .
```
 
---
 
## Run the Container
 
```bash
docker run -d -p 127.0.0.1:<host_port>:8000 --env-file .env --name vrms-container vrms-image gunicorn config.wsgi:application --bind 0.0.0.0:8000
```
---
 
## Managing the Container
 
Check it is running:
 
## Migrations in Production
 
Run migrations against the production database:
 
```bash
docker run --rm --env-file .env vrms-image python manage.py migrate
```
 
> Always run migrations before starting the container when deploying a new version.
