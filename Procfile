release: python manage.py migrate
web: gunicorn django_movie.wsgi --log-file - --log-level debug
