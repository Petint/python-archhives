import json
from autotable import Table

jsonfile = open("427520.json", 'rt')
jsondata = json.load(jsonfile)
jsonfile.close()
print(jsondata)

json_table = Table(jsondata)
print(json_table.make())
