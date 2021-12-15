# import pandas as pd

# df = pd.read_excel('sepomex/sepomexdata.xls', sheet_name=['Distrito_Federal'])

# df.to_json(path_or_buf='Distrito_Federal.json', orient='records')
import excel2json

excel2json.convert_from_file('sepomex/sepomexdata.xls')
