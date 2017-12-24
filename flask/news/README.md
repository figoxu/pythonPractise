http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application

brew install mysql
pip3 install flask_sqlalchemy
#pip3 install PyMySQL
sudo pip3 install flask_sqlalchemy
sudo pip3 install mysqlclient
sudo pip3 install PyMongo


from app import db
db.create_all()
from app import Doc
doca = Doc("Hello Java","File Content - Java is cool!","2017-08-09 12:00:00")
docb = Doc("Hello Python","File Content - Python is cool!","2017-09-09 12:00:00")
db.session.add(doca)
db.session.add(docb)
db.session.commit()
doca.add_tag('tech')
doca.add_tag('java')
doca.add_tag('linux')
docb.add_tag('tech')
docb.add_tag('python')

print doca.tags