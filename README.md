# 📘 Django Learning Project

A basic Django project built while learning backend development using the Django framework.

This project is created to understand Django fundamentals including project structure, routing, views, models, database migrations, and admin panel usage.

---

## 🚀 Tech Stack

- Python 3.x
- Django
- SQLite (Default Django Database)

---

## 📂 Project Structure

```
Project/
│
├── manage.py
├── config/              # Main project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/            # Django application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd Project
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧠 Learning Objectives

- Understanding Django project structure
- Creating Django apps
- URL routing with `urls.py`
- Writing views
- Returning `HttpResponse`
- Creating models
- Running migrations
- Using Django Admin Panel

---

## 🎯 Future Improvements

- Add Django REST Framework (DRF)
- Implement authentication system
- Connect with React frontend
- Deploy to cloud (Render / Railway / AWS)

---

## 👨‍💻 Author

**Shivam Kumar Dubey**  
Backend Developer | QA Engineer  

GitHub: https://github.com/shivamdubey023  
LinkedIn: https://www.linkedin.com/in/shivam-kumar-dubey-970a87248  

---

⭐ This project is part of my backend development learning journey.