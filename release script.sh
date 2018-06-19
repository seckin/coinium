echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc

mkvirtualenv mysite
pip3 install django
pip3 install requests
pip3 install mysqlclient
pip3 install pymysql
cd ~

rm -rf ~/coinium
rm -rf ~/mysite
git clone https://seckin:co1n23im@github.com/seckin/coinium.git
mv coinium/mysite/ ./

printf "\n\nDATABASES = {'default': {'ENGINE': 'django.db.backends.mysql','OPTIONS': {'read_default_file': '/root/mysql.cnf',},}}" >> ~/mysite/mysite/settings.py

cd ~/mysite
~/mysite/manage.py migrate
# ~/mysite/manage.py createsuperuser


printf '\n\nALLOWED_HOSTS = ["104.131.139.250", "coinium.app"]' >> ~/mysite/mysite/settings.py
printf "\n\nSTATIC_ROOT = os.path.join(BASE_DIR, 'static/')" >> ~/mysite/mysite/settings.py
printf '\n\nSPREADS_DB_NAME = "coinim"' >> ~/mysite/mysite/settings.py


~/mysite/manage.py collectstatic

sudo ufw allow 8080
#~/mysite/manage.py runserver 0.0.0.0:8080

uwsgi --http :8080 --home /root/Env/mysite --chdir /root/mysite --wsgi-file /root/mysite/mysite/wsgi.py

