from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Johnny Sokol'}
    posts = [
        {
            'author': {'username': 'Bill'},
            'body': 'I\'m from the wild west'
        },
        {
            'author': {'username': 'Ben'},
            'body': 'lobba lobba lobba'
        }
    ]
    return render_template('index.html', title='Home',user=user, posts=posts)