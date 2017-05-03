#/usr/bin/gunicorn  --chdir /home/null/flask_blog  -c /home/null/flask_blog/gun.py manage:app
/usr/bin/gunicorn -D --chdir /home/null/flask_blog  -c /home/null/flask_blog/gun.py manage:app
