
sudo pip3 install flask flask-sqlalchemy mysqlclient flask-migrate flask-wtf flask-login

$ sudo service mysql start
$ mysql -uroot
> create database simpledu;
$ export FLASK_APP=manage.py
$ export FLASK_DEBUG=1

# 使用 flask-migrate 初始化数据库
$ flask db init
$ flask db migrate -m 'init database'
$ flask db upgrade



$ flask shell
>>> from simpledu.models import db, User
>>> user = User(username='admin',email='admin@shiyanlou.com', password='shiyanlou',role=30)
>>> db.session.add(user)
>>> db.session.commit()