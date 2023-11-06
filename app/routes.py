from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, AddForm

@app.route('/login' , methods=['GET', 'POST'])
def login():
   """login URL"""
   form  = LoginForm()
   if form.validate_on_submit():
      flash(f'You are requesting to login in {form.username.data}')
      return redirect (url_for ('shop'))

   return render_template ('login.html', title='login', form=form)


@app.route('/register' , methods=['GET', 'POST'])
def register():
   """Register URL"""
   form  = RegisterForm()
   if form.validate_on_submit():
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

