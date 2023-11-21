vagrant up 
vagrant ssh 
cd /vagrant
python -m venv ~/venv
source ~/venv/bin/activate

python manage.py runserver 0.0.0.0:8000

