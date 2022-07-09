web: gunicorn django_movie.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
