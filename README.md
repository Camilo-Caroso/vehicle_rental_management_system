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
docker build -t vrms .
```

Run the container with live reload:

```bash
docker run --rm -p 3004:8000 -v $(pwd):/app vrms
```

The API will be available at `http://localhost:3004`.

> Only rebuild the image when you change `requirements.txt`. For code changes, the volume mount handles live reload automatically.

---

## Migrations

Migrations are how Django manages your database schema. When you change your models, you need to run two commands:

**Generate the migration file** (does not touch the database, just creates the file):

```bash
docker run --rm -v $(pwd):/app vrms python manage.py makemigrations
```

**Apply the migrations to the database** (actually creates/updates the tables):

```bash
docker run --rm -v $(pwd):/app vrms python manage.py migrate
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

> To be documented.
