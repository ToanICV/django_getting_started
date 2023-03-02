# Installation
$ pipenv install django
$ pipenv install djangorestframework

# Create a project
$ django-admin startproject [proj_name] [directory]
$ django-admin startapp [app_name] [directory]

# Sync project and app
$ python manage.py migrate

# Try to run
$ python manage.py runserver

# Them package vao list INSTALLED_APPS trong settings.py:
- App name -> ex: demo_app, bat buoc phai lam ngay khi tao app
- Necessary packages -> ex: rest_framework

# Explaintation
- models : lam viec voi database
- serializer: chuyen queryset hoac model cua django thanh dang du lieu de dang render hon tren web va nguoc lai
- api: xu ly phan logic

# Khi co thay doi can apply
$ python manage.py makemigrations
$ python manage.py migrate

# Tao Tai khoan
