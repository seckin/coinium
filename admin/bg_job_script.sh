#echo co1n23ium |su -c "cd /home/seckin/ && workon mysite && cd /home/seckin/mysite && python3.5 manage.py process_tasks" seckin
#co1n23ium
cd /home/seckin/
workon mysite
cd /home/seckin/mysite
python3.5 manage.py process_tasks >/dev/null 2>&1 &