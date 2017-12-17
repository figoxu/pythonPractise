#coding=utf-8
#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/name")
def my_name():
    return 'Figo.xu!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)