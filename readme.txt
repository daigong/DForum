0 pip install -r requirements.txt

1 mysql: CREATE DATABASE lbforum_bbs DEFAULT CHARACTER SET utf8;

2 python manage.py syncdb --noinput --migrate

3 python manage.py createsuperuser

4 python manage.py runserver



