from flask import render_template, redirect, url_for, flash, request, jsonify
from flask.helpers import flash
import flask_login
# import linked_list
import requests
from sepomex.__init__ import app, db
from sepomex.models import User, States, Records
from sepomex.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from sepomex.json_read import states, load_json

from sepomex.sepomexextractinfo import data


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/api/welcome', methods=['GET'])
@login_required
def api_welcome():
        
        return jsonify({'message':'Bienvenido a la API'})

@app.route('/api/sepomex/one/<id>', methods=['GET'])
@login_required
def get_one_state(id: int):
    # Consultas a la base de datos
    state = States.query.get_or_404(id)
    return {'name': state.name, 'data': state.data}


    # Con librerias
    # state = States.query.all()
    # all_states_ll = linked_list.LinkedList()

    # for place in states:
    #     all_states_ll.insert_beginning(
    #         {
    #             "id": place.id,
    #             "name": place.name,
    #             "records": place.data
    #         }
    #     )
    
    # response = all_states_ll.get_user_by_id(state_name)
    # return jsonify(response), 200

    # Extraer información desde el DataFrame de pandas
    # response = data[state].to_json()
    # response
    # Para leer información desde los archivos json que fueron extraido por script
    # path = f'sepomex/json/{state}.json'
    # response = load_json(path)
    # return response

@app.route('/api/add/record', methods=['POST'])
@login_required
def add_record():
    record = Records(
        codigo_postal = request.json['codigo_postal'],
        asentamiento = request.json['asentamiento'],
        tipo = request.json['tipo'],
        state = request.json['estado']
    )   
    db.session.add(record)
    db.session.commit()
    return {'id', record.id}, 200


# Rutas de usuarios

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
        flash(f'Cuenta creada con éxito! Has iniciado sesión como: {user_to_create.username.capitalize()}', category='success')

        return redirect(url_for('api_welcome'))
    
    if form.errors != {}: # Si hay errores de validación
        for err_msg in form.errors.values():
            flash(f'Hubo un error al crear el usuario:--{err_msg}', category='danger')

    return render_template('users/register.html',form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Enhorabuena! Has iniciado en la sesión: {attempted_user.username.capitalize()}', category='success')
            return redirect(url_for('api_welcome'))

        else:
            flash('Usuario y contraseña no coinciden, Favor de intentar nuevamente.', category='danger')

    return render_template('users/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Has salido de tu sesión', category='info')
    return redirect(url_for('home'))
