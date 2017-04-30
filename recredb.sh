rm data-dev.sqlite
rm migrations/ -rf
./manage.py db init
./manage.py db migrate -m "initial migration"
./manage.py db upgrade
