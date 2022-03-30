import os
import json

curDir = os.path.dirname(__file__)
letter_list = []

def readFile(tempPath=None):

    if tempPath != None:
        with open(tempPath, 'r', encoding='utf-8') as rf:
            fileLines = rf.readlines()

        newLine = ''
        for line in fileLines:
            line0 = line.strip()
            if line0 != '':
                letter_list.append(line0.strip())
                newLine += f'{line0}\n'

        rf.close()

        return newLine

def writeLine(tempPath=None, contents=''):
    if tempPath != None:
        with open(tempPath, 'w', encoding='utf-8') as wf:
            wf.writelines(contents)
        wf.close()


def getExtension(fileName=None):
    if fileName != None:
        nameList = fileName.split('.')
        if len(nameList) > 1:
            return nameList[-1]

    

def getLetterList(filePath=f'{curDir}/input.txt'):
    fileList = [filePath]
    formatted_path_list = []
    if os.path.isfile(filePath):
        tempDir, fil = os.path.split(filePath)
        fileSplitList = filePath.split(".")
        if len(fileSplitList) > 0 :
            newContent = readFile(tempPath=filePath)
            outputPath = f"{tempDir}/formatted_{fil}".replace('\\', "/")
            writeLine(tempPath=outputPath, contents=newContent)
            return letter_list


def getLetterListJSON(jsonPath=f'{curDir}/input.json'):
    with open(jsonPath, 'r', encoding='utf-8') as jo:
        jsonOb = json.load(jo)
    # mainDict = json.loads(jsonOb)
    mainDict = jsonOb
    return list(mainDict.keys()), mainDict

if __name__ == '__main__':
    print(getLetterList(filePath='E:\DATA_ANL - Copy\BANGLA_QA\input.txt'))
