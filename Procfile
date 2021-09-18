release: python manage.py makemigration --no-input
release: python manage.py migrate--no-input
release: source .env
heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn project.wsgi