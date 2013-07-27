-2

sudo apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev libpng12-dev

#虚拟环境需要lib映射
cd $VIRTUAL_ENV/lib
ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so libjpeg.so
ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so libfreetype.so
ln -s /usr/lib/x86_64-linux-gnu/libpng.so  libpng.so
ln -s /usr/lib/x86_64-linux-gnu/libz.so   libz.so 


apt-get install python-dev

-1 sudo apt-get install libmysqlclient-dev 

0 pip install -r requirements.txt

1 mysql: CREATE DATABASE lbforum_bbs DEFAULT CHARACTER SET utf8;

2 python manage.py syncdb --noinput --migrate

3 python manage.py createsuperuser

4 python manage.py runserver 0.0.0.0:8000



