from app import app, db
from app.models import User
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, AddForm
from flask_login import login_user

@app.route('/login' , methods=['GET', 'POST'])
def login():
   """login URL"""
   form  = LoginForm()
   if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user is None or not user.check_password(form.password.data):
         flash('Invalid username or Password')
         return redirect(url_for ('login'))
      login_user(user, remember= form.remember_me.data)  
      flash(f'Welcome {form.username.data}')
      return redirect (url_for ('shop'))

   return render_template ('login.html', title='login', form=form)


@app.route('/register' , methods=['GET', 'POST'])
def register():
   """Register URL"""
   form  = RegisterForm()
   if form.validate_on_submit():
      user = User(username= form.username.data)
      user.set_password(form.password.data)
      db.session.add(user)
      db.session.commit()
      flash(f'You are requesting to login in {form.username.data}')
      return redirect (url_for ('login'))

   return render_template ('register.html', title="Register", form=form)
   


@app.route('/')
@app.route('/home')
def shop():
   """ URL"""
   return render_template ('shop.html', title="Shop")

@app.route('/add' , methods=['GET', 'POST'])
def add():
   """add product URL"""
   form  = AddForm()
   if form.validate_on_submit():
      flash(f'Your product has been saved ')
      return redirect (url_for ('shop'))

   return render_template ('add.html', title='Add Product', form=form)

