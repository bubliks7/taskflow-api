# 🚀 TaskFlow API

REST API do zarządzania projektami i zadaniami (inspirowane Trello).

## 🔧 Technologie

* Python
* Django
* Django REST Framework
* JWT Authentication
* Docker

---

## ✨ Funkcjonalności

* Rejestracja i logowanie użytkownika (JWT)
* Tworzenie projektów
* Dodawanie członków do projektów
* Tworzenie i zarządzanie taskami
* Przypisywanie tasków do użytkowników
* Filtrowanie tasków (status, priority, project)
* System uprawnień:

  * tylko owner lub member widzi projekt
  * tylko owner/member może dodać task
  * brak dostępu do чужych projektów

---

## 🔐 Autoryzacja

API używa JWT.

W nagłówku:
Authorization: Bearer <token>

---

## 📦 Endpointy

### Auth

* POST /api/token/ – logowanie

---

### Projects

* GET /api/projects/
* POST /api/projects/
* PUT /api/projects/<id>/
* DELETE /api/projects/<id>/

---

### Tasks

* GET /api/tasks/
* POST /api/tasks/
* GET /api/tasks/<id>/
* PUT /api/tasks/<id>/
* DELETE /api/tasks/<id>/

---

## 🔍 Filtrowanie

Możesz filtrować taski:

* /api/tasks/?status=TODO
* /api/tasks/?priority=HIGH
* /api/tasks/?project=1

---

## 🐳 Uruchomienie (Docker)

```bash
docker compose build
docker compose up
```

---

## 🧠 Autor

Projekt wykonany jako projekt portfolio backend (junior).
