# Taskflow 🗂️

> ⚠️ **Work in progress** — this project is currently under active development and not yet complete.

A task management application with user control, task assignment and status tracking.

---

## 🚀 Tech Stack

- **Backend:** FastAPI + PostgreSQL + SQLAlchemy + Alembic
- **Frontend:** React + Vite
- **Infrastructure:** Docker + Docker Compose

---

## 📦 Project Structure

```
📁 backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── database.py
│   └── alembic/
📁 frontend/
│   └── src/
📁 db/
│   └── postgres_data/
📄 docker-compose.yml
```

---

## 🧱 Data Model

- **User:** id, name, email, created_date
- **Task:** id, title, description, priority, expiry_date
- **Status:** id, description
- **User_Task:** user_id, task_id, date_of_assignment
- **Status_Task:** task_id, status_id, date

---

## 🧪 Running the Project

```bash
git clone https://github.com/federicovalino/Taskflow.git
cd Taskflow
docker-compose up --build
```

- FastAPI docs: http://localhost:8000/docs
- React frontend: http://localhost:5173
- PostgreSQL: port 5432
