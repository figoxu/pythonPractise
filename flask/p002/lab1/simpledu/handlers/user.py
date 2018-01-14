from flask import Blueprint, render_template
from simpledu.models import User,Course

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/<username>')
def detail(username):
    u = User.query.filter(User.username==username).first_or_404()
    cs = Course.query.filter(Course.author_id==u.id).all()
    return render_template('user.html',user=u, courses=cs)

