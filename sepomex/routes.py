from flask import render_template, redirect, url_for, flash, request, jsonify
from flask.helpers import flash
import flask_login
from sepomex.__init__ import app, db
from sepomex.models import User, States, Records
from sepomex.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from sepomex.json_read import states, load_json
from sepomex.schemas import RecordSchema, UserSchema, StateSchema, StateSchemaNoRel

from sepomex.sepomexextractinfo import data

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# API

@app.route('/api/welcome', methods=['GET'])
@login_required
def api_welcome():
    """Da la bievenida para que el usuario sepa que ahora tiene acceso a la ap"""

    return jsonify({'message':'Bienvenido a la API'})

# Rutas de Estados API

@app.route('/api/get/one/state/<state_name>', methods=['GET'])
@login_required
def get_one_state(state_name: str):
    """Obtener los datos de los estados y la data de la que corresponde cada registro (regresa id)  """

    state = States.query.filter_by(name=state_name).first()
    state_schema = StateSchema()
    dump_data = state_schema.dump(state)
    return jsonify(dump_data)

@app.route('/api/get/all_states', methods=['GET'])
@login_required
def get_all_states():
    """Obtener todos los estados"""

    states = States.query.all()
    state_schema = StateSchemaNoRel(many=True)
    dump_data = state_schema.dump(states)
    return jsonify(dump_data)

# Rutas de Usuario API
@app.route('/api/get/user/<name>', methods=['GET'])
@login_required
def get_user(name: str):
    """Obtener información de un usuario"""
    user = User.query.filter_by(username=name).first()
    user_schema = UserSchema()
    output = user_schema.dump(user)
    return jsonify({'user':output})

@app.route('/api/get/all_users', methods=['GET'])
@login_required
def get_users():
    """Obtener información de todos los usuarios en la base"""
    users = User.query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(users)
    return jsonify({'users':output})

@app.route('/api/post/record', methods=['POST'])
@login_required
def add_record():
    """Añadir un nuevo registro"""
    record = Records(
        codigo_postal = request.json['codigo_postal'],
        asentamiento = request.json['asentamiento'],
        tipo = request.json['tipo'],
        state = request.json['estado']
    )   
    db.session.add(record)
    db.session.commit()
    return {'id', record.id}, 200

# Rutas de Registros
@app.route('/api/get/record/<record_id>', methods=['GET'])
@login_required
def get_record_by_id(record_id: int):
    """obtener información de un registro"""
    record = Records.query.filter_by(id=record_id).first()
    record_schema = RecordSchema()
    output = record_schema.dump(record)
    return jsonify({'Registro':output})

@app.route('/api/get/records_from/<state_id>', methods=['GET'])
@login_required
def get_records_by_state_id(state_id: int):
    "Obtener todos los registros que corresponden a un estado"
    records = Records.query.filter_by(estado_id=state_id).all()
    record_schema = RecordSchema(many=True)
    output = record_schema.dump(records)
    return jsonify({'Registros':output})

# Rutas de usuarios

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registrar a nuevo usuario"""
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
    """Inicio de sesion de usuario"""
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
    """Cerrar session del usuario"""
    logout_user()
    flash('Has salido de tu sesión', category='info')
    return redirect(url_for('home'))
