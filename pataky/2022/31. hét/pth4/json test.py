import json

jsonfile = open("example.json", 'rt')
jsondata = json.load(jsonfile)
print(jsondata)
