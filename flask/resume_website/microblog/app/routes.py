from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Jorge'},
            'body': 'Que frío hace hoy en Madrid!'
        },
        {
            'author': {'username': 'Emma'},
            'body': 'Cats and dogs and dogs and cats.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
