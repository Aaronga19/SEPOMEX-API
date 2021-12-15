import json
import os 


def load_json(path):
    with open(path) as f:
        data = json.load(f)
        return data


states = os.listdir('sepomex/json')
# for state in states:
#     path = f'sepomex/json/{state}'
#     print(state)
#     load_json(path)
            
    