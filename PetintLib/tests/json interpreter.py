import json
# from autotable import Table

jsonfile = open("427520.json.json", 'rt')
jsondata = json.load(jsonfile)
print(jsondata)
