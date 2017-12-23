#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:xujianhui0915@192.168.0.182:3306/shiyanlou?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Doc(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=True)
    content = db.Column(db.String(1024))
    created_time = db.Column(db.String(30))

    def __init__(self,title,content,create_time):
        self.title=title
        self.content=content
        self.created_time=create_time

    def __repr__(self):
        return '<Doc %r>' % self.title

@app.route("/")
def index():
    items=Doc.query.all()
    return render_template("index.html",items=items)

@app.route('/files/<file_id>')
def file(file_id):
    item=Doc.query.filter_by(id=file_id).first()
    if item == None :
        abort(404)
    return render_template("file.html",item=item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

