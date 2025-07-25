# kpa-backend-assignment-vineetha
Backend assignment for Sarva Suvidhan Pvt. Ltd. (Implemented using Django + PostgreSQL)

This project implements 3 APIs from the KPA Form submission system using Django REST Framework.

## ✅ Implemented APIs
1. `POST /api/forms/wheel-specifications`
2. `GET /api/forms/wheel-specifications` (with filters)
3. `POST /api/forms/bogie-checksheet`

## 🚀 Tech Stack
- Python 3.8
- Django 4.2
- Django REST Framework
- PostgreSQL
- dotenv for config

## 🛠️ Setup Instructions

```bash
# Create virtual env
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Setup PostgreSQL DB & .env file
cp .env.example .env

# Migrate
python manage.py migrate

# Run server
python manage.py runserver
