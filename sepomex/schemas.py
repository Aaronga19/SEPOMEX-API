from flask_sqlalchemy import model
from sepomex.__init__ import ma
from sepomex.models import User, States, Records


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships= True

class StateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = States
        include_relationships= True
        load_instance = True

class StateSchemaNoRel(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = States
        load_instance = True

class RecordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Records
        load_instance = True
        include_fk = True
