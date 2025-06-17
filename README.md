# Micro Backend - Django REST API

A Django REST API backend service built with Poetry for dependency management.

## Setup

1. Install dependencies:

   ```bash
   poetry install
   ```

2. Activate the virtual environment:

   ```bash
   poetry shell
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Development

- Python 3.12+
- Django 4.2+
- Django REST Framework 3.16+

## Project Structure

```
micro-backend/
├── micro_backend/          # Main Django project
├── pyproject.toml         # Poetry configuration
└── README.md             # This file
```
