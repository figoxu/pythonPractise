#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/shiyanlou?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
client = MongoClient('127.0.0.1',27017)
mgoDb = client.shiyanlou

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

    def add_tag(self, tag_name):
        # 读取 mongodb，返回当前文章的标签列表
        # if mgoDb.tag.find_one({'_id':self.id}) == None :
        #     mgoDb.tag.insert_one({'_id': self.id,'tag':[tag_name]})
        # else:
        mgoDb.tag.update({'_id':self.id},{'$addToSet':{'tag':tag_name}},upsert=True)

    def remove_tag(self,tag_name):
        # 读取 mongodb，返回当前文章的标签列表
        mgoDb.tag.update({'_id':self.id},{'$pull':{'tag':tag_name}})

    @property
    def tags(self):
        # 读取 mongodb，返回当前文章的标签列表
        v=mgoDb.tag.find_one({'_id':self.id})
        return v['tag']

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

