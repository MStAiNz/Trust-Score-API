# Copilot Instructions for Trust Score API

## Project Overview
This is a Django-based REST API for managing and calculating trust scores. The main components are:
- `trust_score/`: Django project settings and root URLs.
- `reputation/`: Django app containing models, views, serializers, and app-specific URLs for trust score logic.

## Architecture & Data Flow
- **Models**: Defined in `reputation/models.py`. Trust scores and related entities are stored in the default SQLite database (`db.sqlite3`).
- **Views**: API endpoints are implemented in `reputation/views.py` using Django REST Framework patterns.
- **Serializers**: Data validation and transformation handled in `reputation/serializers.py`.
- **URLs**: App-level routing in `reputation/urls.py`, project-level routing in `trust_score/urls.py`.
- **Migrations**: All schema changes tracked in `reputation/migrations/`.

## Developer Workflows
- **Run Server**: `python manage.py runserver` from the `trust_score/` directory.
- **Apply Migrations**: `python manage.py migrate`
- **Create Migrations**: `python manage.py makemigrations reputation`
- **Run Tests**: `python manage.py test reputation`
- **Debugging**: Use Django's built-in error pages and logging. No custom debug tooling detected.

## Patterns & Conventions
- **App Structure**: Follows standard Django app layout. All business logic for trust scores is in the `reputation` app.
- **REST API**: Uses Django REST Framework conventions for views and serializers.
- **Naming**: Models, views, and serializers are named for clarity (e.g., `TrustScore`, `TrustScoreSerializer`).
- **Migrations**: Always keep migrations up to date with model changes.

## Integration Points
- **Database**: SQLite (`db.sqlite3`) by default. No external DB detected.
- **External APIs**: No integrations found in codebase.
- **Dependencies**: Django, Django REST Framework (check `requirements.txt` if present).

## Examples
- To add a new trust score field, update `reputation/models.py`, run `makemigrations`, then `migrate`.
- To expose a new API endpoint, add a view in `reputation/views.py`, serializer in `serializers.py`, and route in `urls.py`.

## Key Files
- `trust_score/settings.py`: Project configuration
- `reputation/models.py`: Data models
- `reputation/views.py`: API logic
- `reputation/serializers.py`: Data validation
- `reputation/urls.py`: App routes

---
For questions or unclear patterns, ask for clarification or examples from maintainers.
