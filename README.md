#  Book Management

## Overview  

This project is a **full-stack book management system** that includes:  

- **Frontend**: An Angular application for managing books.  
- **Backend**: A FastAPI-based REST API for book storage and management.  
- **PostgreSQL**: A database for persistent book storage.  

Both services are containerized and can be easily deployed using **Docker Compose**.  

---

## 🛠 Tech Stack  

### 🔹 Frontend  

- **Angular** (Frontend Framework)  
- **TypeScript** (Programming Language)  
- **Ng-Zorro Ant Design** (UI Components)  

### 🔹 Backend  

- **FastAPI** (Web Framework)  
- **SQLAlchemy** (ORM)  
- **Pydantic** (Validation)  
- **PostgreSQL** (Database)  
- **Pytest** & **Testcontainers** (Testing)

### 🔹 Database

- **AWS RDS**

### 🔹 DevOps  

- **Docker & Docker Compose** (Containerization)  

---

## Features  

✔️ View a list of books  
✔️ Add new books  
✔️ Edit existing books  
✔️ Delete books  
✔️ Mark books as read/unread  

---

## 🐳 Running with Docker Compose  

### 1️. Clone the repository  
```sh
git clone https://github.com/t1xgo/book-app.git
cd book-app
```

### 2️. Run the application  
```sh
docker-compose up --build
```
- The **frontend** will be available at: **`http://localhost:4200`**  
- The **backend API** will be available at: **`http://localhost:8000`**  
- Open **Swagger UI** for API documentation: **`http://localhost:8000/docs`**  

### 3️. Stop the application  
```sh
docker-compose down
```

---

## 🛠 Running Locally Without Docker  

### 🔹 Backend (FastAPI)  
```sh
cd book-api
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate venv (Mac/Linux)
venv\Scripts\activate  # Activate venv (Windows)
pip install -r requirements.txt  # Install dependencies
uvicorn app.main:app --reload  # Start API
```
API available at: **`http://127.0.0.1:8000`**  

### 🔹 Frontend (Angular)  
```sh
cd book-client
npm install  # Install dependencies
ng serve  # Start frontend
```
Frontend available at: **`http://localhost:4200`**  

---

## 📖 API Endpoints  

| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| GET    | `/books`        | Get all books |
| POST   | `/books`        | Create a new book |
| PUT    | `/books/{id}`   | Update a book |
| DELETE | `/books/{id}`   | Delete a book |
| GET    | `/health`       | Get app status  |

---

## ✅ Running Tests  

### 🔹 Backend Tests  
```sh
cd book-api
pytest tests
```

### 🔹 Postman Tests integration
![Image](https://github.com/user-attachments/assets/5755fdec-c803-4b6a-a713-e215bb89a667)

![Image](https://github.com/user-attachments/assets/a3857caf-16b0-49bc-b7b9-e5938f20ed26)

You can import the collection and environment variables of postman if you want to test it by yourself,
It will be in a folder called Postman.zip.

---

### ✨ Author  
- **Santiago Cano**  

