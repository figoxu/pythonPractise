#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,render_template,abort
import json
import os.path
from collections import namedtuple

app = Flask(__name__)

NewItem = namedtuple("NewItem",['filename',"title","create_time","content"])


@app.route("/")
def index():
    files = os.listdir("./files")
    items = []
    for file in files :
        data = readJsonData(file)
        short_name=file.split(".")[0]
        item = NewItem(short_name,data['title'],data['created_time'],data['content'])
        items.append(item)
    return render_template("index.html",items=items)

def readJsonData(filename):
    with open('./files/'+filename) as f:
        return json.loads(f.read())

@app.route('/files/<filename>')
def file(filename):
    if not os.path.exists('./files/'+filename):
        abort(404)
    fullpath = filename+".json"
    data = readJsonData(fullpath)
    item = NewItem(filename,data['title'],data['created_time'],data['content'])
    return render_template("file.html",item=item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

