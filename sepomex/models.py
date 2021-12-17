from sepomex.__init__ import db, bcrypt, login_manager

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    " Modelo de tabla de usuarios para acceder a la api"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'Item: {self.username}'


class States(db.Model):
    "Tabla para entidades de la república"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    data = db.relationship('Records', backref="state", lazy=True)

    def __repr__(self):
        return f'Item: {self.name}'


class Records(db.Model):
    "Tabla de registros de cada una de los lugares de cada estado"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    codigo_postal = db.Column(db.Integer(), nullable=False, unique=False)
    asentamiento = db.Column(db.String(length=200), nullable=False, unique=False)
    tipo = db.Column(db.String(length=50), nullable=True, unique=False)
    estado_id = db.Column(db.Integer(), db.ForeignKey('states.id')) # Se relacionan los datos correspondientes a cada estado

    
    

