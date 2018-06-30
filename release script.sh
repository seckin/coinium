su seckin

#echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
#echo "export WORKON_HOME=~/Env" >> ~/.bashrc
#echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
#source ~/.bashrc

cd ~
workon mysite
pip3 install django
pip3 install requests
pip3 install mysqlclient
pip3 install pymysql
pip3 install pyquery
pip3 install django-background-tasks
pip3 install django-silk
pip3 install gunicorn psycopg2


rm -rf ~/coinium
rm -rf ~/mysite
git clone https://seckin:co1n23im@github.com/seckin/coinium.git
mv coinium/mysite/ ./
rm -rf ~/coinium

printf "\n\nDATABASES = {'default': {'ENGINE': 'django.db.backends.mysql','OPTIONS': {'read_default_file': '/home/seckin/mysql.cnf',},}}" >> ~/mysite/mysite/settings.py

cd ~/mysite
~/mysite/manage.py migrate
# ~/mysite/manage.py createsuperuser


printf '\n\nALLOWED_HOSTS = ["104.131.139.250", "95.216.10.109", "coinium.app"]' >> ~/mysite/mysite/settings.py
printf "\n\nSTATIC_ROOT = os.path.join(BASE_DIR, 'static/')" >> ~/mysite/mysite/settings.py
printf '\n\nSPREADS_DB_NAME = "coinim"' >> ~/mysite/mysite/settings.py


~/mysite/manage.py collectstatic

#sudo ufw allow 8080
#~/mysite/manage.py runserver 0.0.0.0:8080

# uwsgi --http :8080 --home /root/Env/mysite --chdir /root/mysite --wsgi-file /root/mysite/mysite/wsgi.py

# pip3 install django gunicorn psycopg2
# (mysite) seckin@amineacoin:~/mysite$ /home/seckin/Env/mysite/bin/gunicorn --bind 0.0.0.0:8000 mysite.wsgi
#(mysiteenv) root@amineacoin:~/mysite# gunicorn --bind 0.0.0.0:8000 mysite.wsgi

killall gunicorn
/home/seckin/gunicorn_script.sh
# killall python
# killall python3
/home/seckin/bg_job_script.sh
# &>/dev/null 2>&1 &
