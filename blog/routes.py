from flask import Flask,render_template, url_for,flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from blog import bcrypt,db
from flask_login import login_user,current_user, logout_user


posts=[

{
	'author':'rakshith',
	'title': 'done',
	'content':'none',
	'date_published': 'Aug 30'
},

{
   'author':'more',
   'title': 'come here',
   'content':'again',
   'date_published': 'Aug 31'
}

]


@app.route("/home")
def home():
	return render_template('home.html',posts=posts,title='home')

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
    	hash_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    	users= User(username=form.username.data, email=form.email.data, password=hash_password)
    	db.session.add(users)
    	db.session.commit()
    	flash(f"{form.username.data} Account is created!! You can now login!!",'success')
    	return redirect(url_for('login'))
    return render_template('register.html',form=form,title='register')

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
              login_user(user,remember=form.remember.data)
              flash("Logged in successfully",'success')
              return redirect(url_for('home'))
             
        else:
            flash("Login unsuccessful..Try again",'danger')      
    return render_template('login.html',form=form,title='login')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))