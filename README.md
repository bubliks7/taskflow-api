🚀 TaskFlow API

A REST API for project and task management (inspired by Trello).

🔧 Tech Stack
    Python
    Django
    Django REST Framework
    JWT Authentication
    Docker
✨ Features
    User registration and login (JWT-based authentication)
    Create and manage projects
    Add members to projects
    Create and manage tasks
    Assign tasks to users
    Task filtering (by status, priority, project)
🔐 Permissions System
    Only the owner or project members can view a project
    Only the owner or members can create tasks
    No access to projects you don’t belong to
🔐 Authentication

    The API uses JWT for authentication.

    Include the token in the request header:

    Authorization: Bearer <your_token>
📦 API Endpoints
🔑 Authentication
    POST /api/token/ – obtain JWT token (login)
📁 Projects
    GET /api/projects/ – list projects
    POST /api/projects/ – create a project
    PUT /api/projects/<id>/ – update a project
    DELETE /api/projects/<id>/ – delete a project
✅ Tasks
    GET /api/tasks/ – list tasks
    POST /api/tasks/ – create a task
    GET /api/tasks/<id>/ – retrieve a task
    PUT /api/tasks/<id>/ – update a task
    DELETE /api/tasks/<id>/ – delete a task
🔍 Filtering

    You can filter tasks using query parameters:

    /api/tasks/?status=TODO
    /api/tasks/?priority=HIGH
    /api/tasks/?project=1
🐳 Running the Project (Docker)
    docker compose build
    docker compose up
🧠 Author

This project was built as a backend portfolio project (junior level).
