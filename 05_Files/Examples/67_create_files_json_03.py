import json

with open('./05_Files/Examples/datos.json') as json_file:  
    data = json.load(json_file)
    p = data['people'][1]
    print('Name: ' + p['name'])
    print('Website: ' + p['website'])
    print('From: ' + p['from'])
    print('')