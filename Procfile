release: python manage.py makemigration --no-input
release: python manage.py migrate--no-input
release: source .env
web: gunicorn project.wsgi