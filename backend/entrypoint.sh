#!/bin/sh

sleep 1

# python manage.py makemigrations
python manage.py migrate

# python manage.py create_default_admin
# python manage.py collectstatic --no-input

# django-admin compilemessages -l en -l ru -l ky

gunicorn core.wsgi:application --bind 0.0.0.0:8000 --access-logfile - --reload -w 4 --timeout 1200