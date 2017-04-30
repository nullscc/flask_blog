rm data-dev.sqlite
rm -rf migrations/
./manage.py db init
./manage.py db migrate -m "initial migration"
./manage.py db upgrade
