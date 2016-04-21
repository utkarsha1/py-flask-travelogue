from app import app
from flask import flash
from flask import redirect
from flask import render_template
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Anu'}  # fake/mock user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!',
            'date': '4/21/2016'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!',
            'date': '3/17/2016'
        },
        {
            'author': {'nickname': 'Renee'},
            'body': 'No fog in SF, it\'s bright, sunny and warm',
            'date': '12/21/2015'
        }
    ]
    return render_template("index.html",
                           title='Travelogue',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
