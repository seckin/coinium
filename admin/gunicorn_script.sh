cd /home/seckin/
workon mysite
cd /home/seckin/mysite
/home/seckin/Env/mysite/bin/gunicorn --access-logfile - --workers 8 --bind unix:/home/seckin/mysite/mysite.sock mysite.wsgi:application &>/var/log/gunicorn_stdout_stderr.log &