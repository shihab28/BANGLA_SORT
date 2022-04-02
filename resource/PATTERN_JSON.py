import json
import os

curDir = os.path.dirname(__file__).replace("\\", "/")
jsonPath = f"{curDir}/class_map_corrected.json".replace("\\", "/")
acceptedJSONPath = f'{curDir}/accepted.json'
rejectedJSOnPath = f'{curDir}/rejected.json'


with open(jsonPath, 'r', encoding='utf-8') as jo:
    jsonOb = json.load(jo)

acceptedJsonDict = {}
with open(acceptedJSONPath, 'r', encoding='utf-8') as jo:
    acceptedJsonDict = json.load(jo)
acceptedJsonKeyList = list(acceptedJsonDict.keys())

rejectedjsonDict = {}
with open(rejectedJSOnPath, 'r', encoding='utf-8') as jo:
    rejectedjsonDict = json.load(jo)
rejectedjsonKeyList = list(rejectedjsonDict.keys())
# print("acceptedJsonDict : ", acceptedJsonDict)
# print("rejectedjsonDict : ", rejectedjsonDict)


# mainDict = json.loads(jsonOb)
mainDict = jsonOb
mainCLassDict = mainDict
# print(mainDict)

new_dictionary = {}

for key1 in mainDict.keys():
    new_dictionary[key1] = {}
    for key2 in mainDict[key1].keys():
        new_dictionary[key1][mainDict[key1][key2]] = key2


# print(json.dumps(new_dictionary, indent=3))

pattern_dictionary = {}
for root in list(new_dictionary["grapheme_root"].keys()):
    pattern_dictionary[root] = {
        'c': -1,
        'r': new_dictionary["grapheme_root"][root],
        'v': -1
    }

# grapheme_root, consonant_diacritic, vowel_diacritic

zeroList = ['0']
leastList = ['1', '8', '9']
mostList = ['2']
rjList = ['3']
urListV = ['4', '5', '6']
urListC = []

new_dictionary_index_letter = {}
new_dictionary_letter_index = {}

curInd = 0
for symb in list(new_dictionary["symbol_diacritic"].keys()):
    pattern_value = symb
    pattern_dictionary[pattern_value] = {
        'c': '',
        'r': '',
        'v': '',
        's': pattern_value
    }

    if pattern_value in acceptedJsonKeyList:
        acceptedJsonDict[pattern_value] = {
        'c': '',
        'r': '',
        'v': '',
        's': pattern_value
    }

    elif pattern_value in rejectedjsonKeyList:
        rejectedjsonDict[pattern_value] = {
        'c': '',
        'r': '',
        'v': '',
        's': pattern_value
    }

    new_dictionary_index_letter[str(curInd)] = symb
    new_dictionary_letter_index[symb] = str(curInd)
    curInd += 1



for root in list(new_dictionary["grapheme_root"].keys())[11:]:
    for consonant in new_dictionary["consonant_diacritic"].keys():
        for vowel in new_dictionary["vowel_diacritic"].keys():
            
            # if new_dictionary["consonant_diacritic"][consonant] in zeroList and new_dictionary["vowel_diacritic"][vowel] not in zeroList:
            #     pattern_value = consonant + root + vowel 
            # elif new_dictionary["consonant_diacritic"][consonant] not in zeroList and new_dictionary["vowel_diacritic"][vowel] in zeroList:
            #     pattern_value = vowel + root + consonant
            # el
            if new_dictionary["consonant_diacritic"][consonant] in leastList:
                pattern_value = root + vowel + consonant
            elif new_dictionary["consonant_diacritic"][consonant] in mostList:
                pattern_value = consonant + root + vowel
            elif new_dictionary["consonant_diacritic"][consonant] in rjList:
                pattern_value = "র্" + root + "্য" + vowel
            else:
                pattern_value = root + consonant + vowel

            pattern_dictionary[pattern_value] = {
                'c': new_dictionary["consonant_diacritic"][consonant],
                'r': new_dictionary["grapheme_root"][root],
                'v': new_dictionary["vowel_diacritic"][vowel],
                's': ''
            }

            if pattern_value in acceptedJsonKeyList:
                acceptedJsonDict[pattern_value] = {
                'c': new_dictionary["consonant_diacritic"][consonant],
                'r': new_dictionary["grapheme_root"][root],
                'v': new_dictionary["vowel_diacritic"][vowel],
                's': ''
            }

            elif pattern_value in rejectedjsonKeyList:
                rejectedjsonDict[pattern_value] = {
                'c': new_dictionary["consonant_diacritic"][consonant],
                'r': new_dictionary["grapheme_root"][root],
                'v': new_dictionary["vowel_diacritic"][vowel],
                's': ''
            }
        
            new_dictionary_index_letter[str(curInd)] = pattern_value
            new_dictionary_letter_index[pattern_value] = str(curInd)
            curInd += 1


# print("acceptedJsonDict : ", acceptedJsonDict)
# print("rejectedjsonDict : ", rejectedjsonDict)

for pattern_value in list(acceptedJsonDict.keys()):
    
    keyS = list(acceptedJsonDict[pattern_value].keys())
    # print(acceptedJsonDict[pattern_value])
    if 's' not in keyS:
        acceptedJsonDict[pattern_value]['s'] = ""
    
    if 'r' not in keyS:
        acceptedJsonDict[pattern_value]['r'] = ""

    if 'v' not in keyS:
        acceptedJsonDict[pattern_value]['v'] = ""

    if 'c' not in keyS:
        acceptedJsonDict[pattern_value]['c'] = ""


for pattern_value in list(rejectedjsonDict.keys()):
    keyS = list(rejectedjsonDict[pattern_value].keys())
    # print(rejectedjsonDict[pattern_value])
    if 's' not in keyS:
        rejectedjsonDict[pattern_value]['s'] = ""
    
    if 'r' not in keyS:
        rejectedjsonDict[pattern_value]['r'] = ""

    if 'v' not in keyS:
        rejectedjsonDict[pattern_value]['v'] = ""

    if 'c' not in keyS:
        rejectedjsonDict[pattern_value]['c'] = ""

dictionary_index_letter = {}
dictionary_index_letter['index_letter'] = new_dictionary_index_letter
dictionary_index_letter['letter_index'] = new_dictionary_letter_index

json_out_file_path = f'{curDir}/input.json'.replace("\\", "/")
json_out_file_path_ind_let = f'{curDir}/index_letter.json'
# json_out_file_path_let_ind = f'{curDir}/letter_index.json'


# print(pattern_dictionary)
# print(type(pattern_dictionary))
# pattern_dictionary = json.dumps(pattern_dictionary, indent=3)

# print("pattern_dictionary : ", type(pattern_dictionary), "\n", pattern_dictionary)
# print("acceptedJsonDict : ", type(acceptedJsonDict), "\n", acceptedJsonDict)
# print("rejectedjsonDict : ", type(rejectedjsonDict), "\n", rejectedjsonDict)

with open(json_out_file_path, 'w', encoding='utf-8') as jo:
    json.dump(pattern_dictionary, jo)
jo.close()

with open(json_out_file_path_ind_let, 'w', encoding='utf-8') as jo:
    json.dump(dictionary_index_letter, jo)
jo.close()

# with open(json_out_file_path_let_ind, 'w', encoding='utf-8') as jo:
#     json.dump(new_dictionary_letter_index, jo)
# jo.close()

with open(acceptedJSONPath, 'w', encoding='utf-8') as jo:
    json.dump(acceptedJsonDict, jo)
jo.close()

with open(rejectedJSOnPath, 'w', encoding='utf-8') as jo:
    json.dump(rejectedjsonDict, jo)
jo.close()


print("***************Pattern Created***************")