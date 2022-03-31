import os, json


curDir = os.path.dirname(__file__).replace("\\", "/")
jsonPath = f"{curDir}/class_map_corrected.json".replace("\\", "/")

with open(jsonPath, 'r', encoding = 'utf-8') as rf:
    jsonOb = json.load(rf)  

    try: 
        jsonDict = json.loads(jsonOb)
    except:
        jsonDict = jsonOb

# print(jsonOb)
# for keyD in jsonDict:
#     if keyD == 'grapheme_root':
#         tempDict = {}
#         tempIndList = list(jsonDict[keyD].keys())
#         for ind, keyS in enumerate(jsonDict[keyD]):
#             if ind >= 2:
#                 tempDict[tempIndList[ind - 2]] = jsonDict[keyD][keyS]

#         jsonDict[keyD] = tempDict


# with open(jsonPath, 'w', encoding = 'utf-8') as wf:
#     json.dump(jsonDict, wf)
# wf.close()