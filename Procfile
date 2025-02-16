release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_root.wsgi:application
