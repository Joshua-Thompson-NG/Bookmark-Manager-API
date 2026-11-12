# Bookmark Manager API

A simple and lightweight RESTful CRUD API for managing bookmarks, built with **FastAPI**, **Python 3.13+**, and **uv**.

---

## Project Overview

The **Bookmark Manager API** provides endpoints to create, read, update, and delete bookmarks. Each bookmark stores essential metadata such as a URL, title, description, and tags to help users organize their saved links.

---

## 🛠️ Tech Stack & Tools

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (with standard dependencies: Uvicorn, Pydantic, etc.)
- **Python Version:** `>=3.13`
- **Package & Environment Manager:** [uv](https://docs.astral.sh/uv/)
- **Linting & Formatting:** [Ruff](https://docs.astral.sh/ruff/)
- **Testing:** [pytest](https://docs.pytest.org/)

---

## 📂 Project Directory Structure

```text
Bookmark-Manager-API/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application instance & router registration
│   ├── database.py      # Database connection & session setup (e.g., SQLite / SQLAlchemy)
│   ├── models.py        # Database ORM models
│   ├── schemas.py       # Pydantic models for request validation & response serialization
│   ├── dependencies.py  # Common FastAPI dependencies (e.g., get_db)
│   └── routers/
│       ├── __init__.py
│       └── bookmarks.py # Bookmark CRUD route handlers
├── tests/
│   ├── __init__.py
│   ├── conftest.py      # Test fixtures & test client setup
│   └── test_bookmarks.py# CRUD unit & integration tests
├── pyproject.toml       # Project metadata, dependencies & tool configs
├── uv.lock              # Lockfile for reproducible environments
└── README.md            # Project documentation & specification
```

---

## Data Model Specification

### Bookmark Attributes

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `id` | `int` | Yes (Generated) | Unique identifier for the bookmark |
| `url` | `str` (HttpUrl) | Yes | Valid URL of the bookmarked resource |
| `title` | `str` | Yes | Short title / name for the bookmark |
| `description` | `str` | No | Optional notes or summary |
| `tags` | `list[str]` | No | Optional tags/categories (e.g. `["python", "docs"]`) |
| `created_at` | `datetime` | Yes (Auto) | Timestamp when the bookmark was created |
---

##  API Endpoints Specification

Base Path: `/api/v1/bookmarks` (or `/bookmarks`)

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **POST** | `/bookmarks/` | Create a new bookmark | `201 Created` |
| **GET** | `/bookmarks/` | List all bookmarks (supports pagination & filtering) | `200 OK` |
| **GET** | `/bookmarks/{id}` | Get a single bookmark by ID | `200 OK` / `404 Not Found` |
| **PUT** / **PATCH** | `/bookmarks/{id}` | Update an existing bookmark | `200 OK` / `404 Not Found` |
| **DELETE** | `/bookmarks/{id}` | Delete a bookmark by ID | `204 No Content` / `404 Not Found` |

### Example Request & Response Payloads

#### 1. Create Bookmark (`POST /bookmarks/`)
**Request Body:**
```json
{
  "url": "https://fastapi.tiangolo.com",
  "title": "FastAPI Documentation",
  "description": "Interactive API docs and tutorials for FastAPI",
  "tags": ["fastapi", "python", "api"]
}
```

**Response (`201 Created`):**
```json
{
  "id": 1,
  "url": "https://fastapi.tiangolo.com",
  "title": "FastAPI Documentation",
  "description": "Interactive API docs and tutorials for FastAPI",
  "tags": ["fastapi", "python", "api"],
  "created_at": "2026-11-12T16:30:00Z"
}
```

#### 2. List Bookmarks (`GET /bookmarks/?skip=0&limit=10&tag=python`)
**Response (`200 OK`):**
```json
[
  {
    "id": 1,
    "url": "https://fastapi.tiangolo.com",
    "title": "FastAPI Documentation",
    "description": "Interactive API docs and tutorials for FastAPI",
    "tags": ["fastapi", "python", "api"],
    "created_at": "2026-11-12T16:30:00Z"}
]
```

---

## Getting Started

### 1. Prerequisites
Ensure you have Python 3.13+ and `uv` installed:
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install Dependencies
```bash
uv sync
```

### 3. Run the Development Server
```bash
uv run fastapi dev app/main.py
```
Or:
```bash
uv run uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### 4. Interactive Documentation
FastAPI provides automatic interactive API documentation:
- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## 🧪 Testing & Code Quality

### Run Tests
```bash
uv run pytest
```

### Run Linter & Formatter
```bash
uv run ruff check .
uv run ruff format .
```
