sudo pip3 install flask flask-sqlalchemy mysqlclient flask-migrate flask-wtf flask-login

# 使用 flask-migrate 初始化数据库
$ flask db init
$ flask db migrate -m 'init database'
$ flask db upgrade