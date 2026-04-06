# 🚀 TaskFlow API

REST API for managing projects and tasks (inspired by Trello).

## 🔧 Technologies

* Python
* Django
* Django REST Framework
* JWT Authentication
* Docker

---

## ✨ Features

* User registration and login (JWT)
* Creating projects
* Adding members to projects
* Creating and managing tasks
* Assigning tasks to users
* Task filtering (status, priority, project)
* Permission system:

  * only owner or member can view a project
  * only owner/member can add tasks
  * no access to other users' projects

---

## 🔐 Authorization

The API uses JWT.

In the header:
Authorization: Bearer <token>

---

## 📦 Endpoints

### Auth

* POST /api/token/ – login

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

## 🔍 Filtering

You can filter tasks:

* /api/tasks/?status=TODO
* /api/tasks/?priority=HIGH
* /api/tasks/?project=1

---

## 🐳 Run (Docker)

```bash
docker compose build
docker compose up
