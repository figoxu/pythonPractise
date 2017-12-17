#coding=utf-8
#!/usr/bin/env python3

from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route("/name")
def my_name():
    return 'Figo.xu!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)