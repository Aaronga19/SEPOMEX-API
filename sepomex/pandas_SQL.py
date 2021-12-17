
from sepomex.sepomexextractinfo import data
from sepomex.models import db, States, Records

# Pruebas de toma de datos
def extractData(data):
    for state in data:
        for i in range(len(data[state])):
            print(f'Estado: {state}')
            print(f"Código Postal: {data[state].iloc[i]['codigo_postal']}")
            print(f"Asentamiento: {data[state].iloc[i]['asentamiento']}")
            print(f"Tipo: {data[state].iloc[i]['tipo']}")

# Script para cargar toda la información del archivo excel a nuestra base de datos en Postgress

def data_to_sql(data):
    # db.drop_all()
    db.create_all()
    
    for state in data:

        site = States(name=state)
        db.session.add(site)
        db.session.commit()
        
        

        for i in range(len(data[state])):
            record = Records(
                codigo_postal=int(data[state].iloc[i]['codigo_postal']),
                asentamiento=data[state].iloc[i]['asentamiento'],
                tipo = data[state].iloc[i]['tipo'],
                state=site
                )
            db.session.add(record)
            db.session.commit()
            
            
        
        

# data_to_sql(data)



# Pruebas con interprete de python 
"""
from sepomex.models import db
db.drop_all()
db.create_all()
from sepomex.models import States, Records
aguascalientes = States(name='Aguascalientes')
print(type(aguascalientes))
db.session.add(aguascalientes)
db.session.commit()
colima = States(name='Colima')
db.session.add(colima)
db.session.commit()


record1 = Records(codigo_postal='00123', asentamiento='Jardines del pedregal', tipo='Colonia', state=aguascalientes)
print(type(record1))
db.session.add(record1)
db.session.commit()
record2 = Records(codigo_postal='57487', asentamiento='Conchita', tipo='Urbano', state=colima)
db.session.add(record2)
db.session.commit()
record3 = Records(codigo_postal='04368', asentamiento='Santocho', tipo='Rural', state=aguascalientes)
db.session.add(record3)
db.session.commit()


aguascal = States.query.filter_by(name='Aguascalientes').first()
aguascal.id
aguascal.name
# aguascal.data
"""