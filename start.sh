python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn jango_deploy.wsgi:application --bind 0.0.0.0:$PORT 