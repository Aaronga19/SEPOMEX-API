from flask import render_template, redirect, url_for, flash, request, jsonify
from flask.helpers import flash
import flask_login
from sqlalchemy.engine import url
from werkzeug.wrappers import response
from sepomex.__init__ import app, db
# from market.models import Item, User
# from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user
from sepomex.json_read import states, load_json


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/get/', methods=['GET'])
def get_info():
        path = f'sepomex/json/Aguascalientes.json'
        response = load_json(path)
        return jsonify(response)
