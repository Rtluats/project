#!/bin/sh

while ! nc -z $SQL_HOST $SQL_PORT ; do
    sleep 0.1
done

python manage.py flush --no-input
python manage.py migrate

exec "$@"