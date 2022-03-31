import os, json


curDir = os.path.dirname(__file__).replace("\\", "/")
jsonPath = f"{curDir}/class_map_corrected.json".replace("\\", "/")

with open(jsonPath, 'r', encoding = 'utf-8') as rf:
    jsonOb = json.load(rf)

jsonDict = json.dumps(jsonOb)
for keyD in jsonDict:
    print(jsonDict[keyD])