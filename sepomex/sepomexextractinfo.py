import pandas as pd

# leer el excel con pandas 
data = pd.read_excel('sepomex/sepomexdata.xls', sheet_name=None, usecols='A:C', names=['codigo_postal', 'asentamiento', 'tipo'])

# print(data['Distrito_Federal'].to_json())


# Extraer cada hoja en un archivo json por separado
"""import excel2json

excel2json.convert_from_file('sepomex/sepomexdata.xls')"""
