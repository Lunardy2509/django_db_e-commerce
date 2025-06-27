# 🛍️ Django DB E-Commerce

A simple e-commerce web application built with Django and MySQL, created as a mid-term project for the **Web-Based Applications** course.

The goal is to connect Django with a MySQL database and render dynamic content in an e-commerce-style front-end.

---

## 📦 Features

- ✅ Fetch product data from MySQL using Django ORM  
- ✅ Render product listings on a styled HTML page  
- ✅ MVC pattern using Django views and templates  
- 🔧 Modular structure for easy extension (e.g. carts, checkout)  

---

## 🛠️ Tech Stack

- **Framework:** Django  
- **Database:** MySQL  
- **Frontend:** HTML, CSS
- **Language:** Python  

---

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/Lunardy2509/django_db_e-commerce.git
cd django_db_e-commerce/Web
```

### 2. Create a virtual environment
```bash
python -m venv env
source env/bin/activate      # macOS/Linux
env\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
⚠️ If you don’t have a `requirements.txt`, run this:
```bash
pip install django mysqlclient
```

### 4. Configure database (MySQL)
Make sure MySQL is running and update the `DATABASES` section in `Web/Web/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 7. Start the development server
```bash
python manage.py runserver
```

Then open your browser and visit:
```markdown
http://127.0.0.1:8000/
```

## 🧪 Tips
- 🔐 Admin Panel: visit `http://127.0.0.1:8000/admin/` to manage data
- 🧱 Use the admin to add/edit product entries
- 🛠️ For MySQL issues, ensure port 3306 is open and user has access

## 📁 Project Structure
```bash
Web/
├── manage.py
├── Web/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── your_app_name/        # likely contains models, views, templates
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── *.html
```

## 📚 Acknowledgments
This project was created as part of a mid-term exam for the Web-Based Applications course. It serves as an introduction to full-stack web development with Django and SQL databases.

## 📬 Contact
- GitHub: [@Lunardy2509](https://github.com/Lunardy2509)
- Email: ferdilunardy@gmail.com

---

Let me know if you'd like help generating a `requirements.txt`, adding badges (like build status or tech stack), or uploading screenshots to include in this README.
