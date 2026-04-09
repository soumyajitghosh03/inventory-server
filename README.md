# 📦 Inventra - Inventory Management System

A production-ready inventory management system built using **FastAPI**, **PostgreSQL**, and **Async SQLAlchemy**.
This project is designed to handle multiple users efficiently with a scalable backend architecture.

---

## 🚀 Tech Stack

* ⚡ FastAPI (Async Backend)
* 🐘 PostgreSQL
* 🧠 SQLAlchemy (Async ORM)
* 🔌 asyncpg (Async DB Driver)
* 🌱 python-dotenv (Environment Management)

---

## 📁 Project Structure

```
server/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── db.py
│   └── ...
│
├── .env
├── .env.example
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd server
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy asyncpg python-dotenv
```

---

## 🔑 Environment Variables Setup

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/inventra
```

---

### ⚠️ Important Notes

* ❌ Do NOT use:

  ```
  postgresql://username:password@localhost:5432/inventra
  ```
* ✅ Always use:

  ```
  postgresql+asyncpg://username:password@localhost:5432/inventra
  ```

👉 Reason:
This project uses **async database engine**, which requires the `asyncpg` driver.

---

### 📌 `.env.example` (for reference)

```
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/inventra
```

---

## ▶️ Run the Server

```bash
uvicorn src.main:app --reload
```

---

## ✅ Expected Output

When the server starts successfully, you should see:

```
⏳ Connecting to database...
✅ DATABASE CONNECTED SUCCESSFULLY
🚀 Application started

INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Test the API

Open your browser:

```
http://127.0.0.1:8000
```

Expected response:

```json
{
  "message": "API is running"
}
```

---

## 🧠 How It Works

* FastAPI runs with an **async lifecycle**
* On startup:

  * Database connection is initialized
* On shutdown:

  * Database connection is safely closed
* All database operations use **non-blocking async queries**

---

## 🔒 Security Best Practices

* ❌ Never commit `.env` file
* ✅ Always use `.env.example` for sharing config format
* 🔐 Keep database credentials private

---

## ⚡ Developer Notes

* Use this command to run the project:

  ```bash
  uvicorn src.main:app --reload
  ```
* Make sure `src` is treated as the root module
* Always use proper async DB URL format

---

## 🚀 Future Roadmap

* User Authentication (JWT)
* Role-Based Access Control
* Inventory Modules (Products, Categories, Stock)
* Dashboard Analytics
* Multi-organization support

---

## 👨‍💻 Author

Soumyajit Ghosh

---


