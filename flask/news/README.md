http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application

brew install mysql
pip3 install flask_sqlalchemy
#pip3 install PyMySQL
 pip3 install mysqlclient



>>> db.create_all()
>>> from app import Doc
>>> doca = Doc("Hello, World!","Hello world! \\\\n This is hello world demo page. \\\\n Please let us know if you have any questions \\\\n Thank you!","2017-08-09 12:00:00")
>>> docb = Doc("Hello, Shiyanlou!","Welcome to shiyanlou.com \\n This is shiyanlou.com louplus demo page. \\n Please let us know if you have any questions \\n Thank you!","2017-09-09 12:00:00")
>>> db.session.add(doca)
>>> db.session.add(docb)
>>> db.session.commit()
