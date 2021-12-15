from flask import render_template, redirect, url_for, flash, request
from flask.helpers import flash
import flask_login
from sqlalchemy.engine import url
from sepomex.__init__ import app, db
# from market.models import Item, User
# from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

