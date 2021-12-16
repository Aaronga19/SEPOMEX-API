from flask import render_template, redirect, url_for, flash, request, jsonify
from flask.helpers import flash
import flask_login
from sqlalchemy.engine import url
from sepomex.__init__ import app, db
from sepomex.models import User
from sepomex.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from sepomex.json_read import states, load_json


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/api.sepomex/', methods=['GET'])
@login_required
def get_info():
        path = f'sepomex/json/Aguascalientes.json'
        response = load_json(path)
        return jsonify(response)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as: {user_to_create.username.capitalize()}', category='success')

        return redirect(url_for('get_info'))
    
    if form.errors != {}: # Si hay errores de validación
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user {err_msg}', category='danger')

    return render_template('users/register.html',form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Enhorabuena! Has iniciado en la sesión: {attempted_user.username.capitalize()}', category='success')
            return redirect(url_for('get_info'))

        else:
            flash('Usuario y contraseña no coinciden, Favor de intentar nuevamente.', category='danger')

    return render_template('users/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out!', category='info')
    return redirect(url_for('home'))
