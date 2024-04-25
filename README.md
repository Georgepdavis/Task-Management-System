Task Management System
Task Management System is a web application designed for efficient task management, built using React for the frontend and Django for the backend, with MySQL as the database. It enables users to manage tasks, assign them, track progress, and collaborate effectively.

Installation
Backend
Navigate to the backend directory:
bash
Copy code
cd backend/myproject1
Install backend dependencies:
bash
Copy code
pip install django django-cors-headers djangorestframework djangorestframework-simplejwt
Make sure MySQL is installed and running.
Configure database settings in settings.py:
python
Copy code
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        'NAME': 'your_database_name',
        'USER': 'your_database_username',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
Run the Django server:
bash
Copy code
python manage.py runserver
Frontend
Navigate to the frontend directory:
bash
Copy code
cd frontend/myproject
Install frontend dependencies:
bash
Copy code
npm install
Usage
Admin
Admin users can register and login.
Admin can perform tasks such as adding, editing, and deleting tasks.
Admin can assign tasks to multiple users and track their progress.
Admin can view completed tasks, add comments, and manage user profiles.
Users
Normal users can register and login.
Users can view tasks assigned to them and submit completed tasks with screenshots.
Users can add comments to tasks and manage their profiles.
Authentication
Authentication is handled using JWT tokens.

Technologies Used
React
Django
MySQL
JWT Authentication


