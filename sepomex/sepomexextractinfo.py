import pandas as pd
#from sepomex.models import db

# leer excel con pandas 
data = pd.read_excel('sepomex/sepomexdata.xls', sheet_name=None, usecols='A:C', names=['codigo_postal', 'asentamiento', 'tipo'])

 
# Añadir registros a base de datos

"""for i in range(len(data['Aguascalientes'])):

    print(data['Aguascalientes'].iloc[i])"""

# for state in data:
#     for data in data[:]:
#         print(f'{data} ')





# print(data['Distrito_Federal'].to_json())


# Extraer cada hoja en un archivo json por separado

"""import excel2json

excel2json.convert_from_file('sepomex/sepomexdata.xls')"""
