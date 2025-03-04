# 📚 FastAPI Book Management API

## 🚀 Project Overview
This project is a simple and efficient REST API built with FastAPI to keep track of books. You can add new books, look them up, update their details, or remove them when you no longer need them.

## 🛠 Tech Stack
- **FastAPI** (Web Framework)
- **SQLAlchemy** (ORM)
- **Pydantic** (Validation)
- **PostgreSQL** (Database)
- **Docker & Docker Compose** (Containerization)
- **Pytest** (Testing)
- **testcontainers** (Database Testing)

---
## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```sh
 git clone https://github.com/t1xgo/book-api.git
 cd book-api
```

### 2️⃣ Create & activate a virtual environment (optional but recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
Create a **.env** file in the root directory and define your database credentials like this:
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/book_db
```

### 5️⃣ Run the application
```sh
uvicorn app.main:app --reload
```
- The API will be available at **`http://127.0.0.1:8000`**
- Open **Swagger UI**: `http://127.0.0.1:8000/docs`

---
## 🐳 Running with Docker

### 1️⃣ Build & Run the containers
```sh
docker-compose up --build
```

### 2️⃣ Stop the containers
```sh
docker-compose down
```

---
## 📖 API Endpoints

### 📌 Books Endpoints
| Method | Endpoint          | Description |
|--------|------------------|-------------|
| GET    | `/books`         | Get all books |
| POST   | `/books`        | Create a new book |
| PUT    | `/books/{id}`   | Update a book |
| DELETE | `/books/{id}`   | Delete a book |

---
## ✅ Running Tests

### 1️⃣ Run Unit Tests
```sh
pytest tests/unit
```

### 2️⃣ Run Integration Tests
```sh
pytest tests/integration
```
---
### ✨ Author
- **Santiago Cano**

