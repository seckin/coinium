cd /home/seckin/
workon mysite
cd /home/seckin/mysite
/home/seckin/Env/mysite/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/seckin/mysite/mysite.sock mysite.wsgi:application &