cd /home/seckin/
workon mysite
cd /home/seckin/mysite
/home/seckin/Env/mysite/bin/gunicorn --access-logfile - --error-logfile /var/log/gunicorn.error.log --log-file /var/log/gunicorn.stdout.log --workers 3 --bind unix:/home/seckin/mysite/mysite.sock mysite.wsgi:application &