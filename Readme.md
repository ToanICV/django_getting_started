### Cài đặt
- pipenv install django
- pipenv install djangorestframework

### Tạo project
- django-admin startproject [proj_name] [directory]
- django-admin startapp [app_name] [directory]

### Đồng bộ project và app
- python manage.py migrate

### Chạy thử 
- python manage.py runserver

### Thêm package vào list INSTALLED_APPS trong settings.py:
- App name -> ví dụ: demo_app, bắt buộc thực hiện lệnh này khi khởi tạo app
- Các packages cần thiết-> ví dụ: rest_framework

### Cập nhật thay đổi
- python manage.py makemigrations
- python manage.py migrate

### Tạo tài khoản admin
python manage.py createsuperuser

### Mô tả hoạt động
- urls: liên kết front-end với back-end
- views: tiếp nhận yêu cầu từ front-end -> xử lý dữ liệu từ models -> trả về json.
- models : làm việc với database
- serializers: chuyển dữ liệu dạng object(Django) của model sang json(Front-end) và ngược lại.
- api: xử lý phần logic
