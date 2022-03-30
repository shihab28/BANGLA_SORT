import json
import os

curDir = os.path.dirname(__file__).replace("\\", "/")
jsonPath = f"{curDir}/class_map_corrected.json".replace("\\", "/")


with open(jsonPath, 'r', encoding='utf-8') as jo:
    jsonOb = json.load(jo)

# print(jsonOb.keys())
mainDict = json.loads(jsonOb)
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


for root in list(new_dictionary["grapheme_root"].keys())[13:]:
    for consonant in new_dictionary["consonant_diacritic"].keys():
        for vowel in new_dictionary["vowel_diacritic"].keys():
            pattern_value = root + vowel + consonant
            pattern_dictionary[pattern_value] = {
                'c': new_dictionary["consonant_diacritic"][consonant],
                'r': new_dictionary["grapheme_root"][root],
                'v': new_dictionary["vowel_diacritic"][vowel]
            }


json_out_file_path = f'{curDir}/input.json'.replace("\\", "/")

with open(json_out_file_path, 'w', encoding='utf-8') as jo:
    json.dump(pattern_dictionary, jo)