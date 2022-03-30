import os
import shutil
import json

from tkinter import *
from tkinter import font

# from PIL import ImageGrab
import pyscreenshot as ImageGrab

import resource.GET_LETTER_LIST as GET_LETTER_LIST

curDir = f"{os.path.dirname(__file__)}/resource".replace("\\", "/")
# inputFilePath = f'{curDir}/input.txt'
inputFilePath = f'{curDir}/input.json'
acceptedFilePath = f'{curDir}/accepted.txt'
rejectedFilePath = f'{curDir}/rejected.txt'
acceptedJSONPath = f'{curDir}/accepted.json'
rejectedJSOnPath = f'{curDir}/rejected.json'
rejectedImageDir = f'{curDir}/rejectedImage'
acceptedImageDir= f'{curDir}/acceptedImage'

# all_letter_list = GET_LETTER_LIST.getLetterList(inputFilePath)
all_letter_list, all_letter_dict = GET_LETTER_LIST.getLetterListJSON(inputFilePath)
accepted_letter_list = []
rejected_letter_list = []
accepted_letter_dict = {}
rejected_letter_dict = {}
print("Total Count : ", len(all_letter_list))
curIndex = 0
# print(all_letter_list)

color_root_bg = '#8B9DC3'
color_root_fg = '#1E1F26'
color_all_bg = '#E1E8ED'
color_all_fg = '#14171A'
color_rej_bg = '#FFCCCC'
color_rej_fg = '#330000'
color_acp_bg = '#CCFFCC'
color_acp_fg = '#003300'
color_lab_bg = '#E4DCF1'
color_lab_fg = '#3D2352'

imageExt = 'png'

def limitMax(val, limVal):
    if val >= limVal:
        return limVal
    return val

def limitMin(val, limVal):
    if val <= limVal:
        return limVal
    return val

font_size = 96

list_height = limitMax(int(font_size*.4), 32)
list_width = limitMax(int(font_size*.25), 15)

canvas_width = limitMax(int(font_size*6.25), 800)
padX = 10
canvas_height = limitMax(int(canvas_width*.5), 400)

root = Tk()
root.config(bg=color_root_bg)
root.title("ACCEPT OR REJECT")
root.minsize(width=list_width*40, height=list_height*15)
root.resizable(width=False, height=False)

font_family_list = font.families()
# Akshar Unicode, Amar Bangla, AdorshoLipi, Nikosh, ChitraMJ, AdarshaLipiCon, AdarshaLipiExp  
# AnandapatraCMJ, AtraiMJ, KumarkhaliMJ', SutonnyMJ, SutonnyOMJ, UrmeeMJ
font_shutonni = font.Font(family='Akshar Unicode', size=limitMax(int(font_size*.15), 10))
font_shutonni_label = font.Font(family='Akshar Unicode', size=font_size, weight=font.BOLD)
font_button = font.Font(family='Arial', size=limitMax(int(font_size*.25), 14), weight=font.BOLD)

def hasKey(tempDIct={}, keyF=None):
    keyList = list(tempDIct.keys())
    if keyF in keyList:
        return True
    return False

def rejectLetter(eve=None):
    global  curIndex, list_letter, list_reject, list_accept, \
        rejected_letter_dict, accepted_letter_dict
    curLet = list_letter.get(curIndex)
    if curLet not in list_reject.get(0, END):
        list_reject.insert(END, curLet)
        list_letter.itemconfig(curIndex,{'bg': color_rej_bg, 'fg' : color_rej_fg})
        rejected_letter_dict[curLet] = all_letter_dict[curLet]

    saveLetter(imageStatus='rejected')


    tempListAcp = list(list_accept.get(0, END))

    if curLet in tempListAcp:  
        if os.path.isfile(f"{acceptedImageDir}/{curLet}.{imageExt}"):
            os.remove(f"{acceptedImageDir}/{curLet}.{imageExt}")
        tempListAcp.remove(curLet)
        list_accept.delete(0, END)        
        if hasKey(accepted_letter_dict, curLet):
            del accepted_letter_dict[curLet]

        for ind, lst in enumerate(tempListAcp):
            list_accept.insert(ind, lst)
            
    nexttLetter()


def acceptLetter(eve=None):
    global  curIndex, list_letter, list_accept, list_reject, \
        rejected_letter_dict, accepted_letter_dict
    curLet = list_letter.get(curIndex)

    if curLet not in list_accept.get(0, END):
        list_accept.insert(END, curLet)
        list_letter.itemconfig(curIndex,{'bg': color_acp_bg, 'fg': color_acp_fg})
        accepted_letter_dict[curLet] = all_letter_dict[curLet]

    saveLetter(imageStatus='accepted')

    tempListRej = list(list_reject.get(0, END))
    if curLet in tempListRej:
        if os.path.isfile(f"{rejectedImageDir}/{curLet}.{imageExt}"):
            os.remove(f"{rejectedImageDir}/{curLet}.{imageExt}")

        tempListRej.remove(curLet)
        list_reject.delete(0, END)
        if hasKey(rejected_letter_dict, curLet):
            del rejected_letter_dict[curLet]

        for ind, lst in enumerate(tempListRej):
            list_reject.insert(ind, lst)
    
    nexttLetter()



def updateLabel(eve=None):
    global  curIndex, list_letter
    curLetter = all_letter_list[curIndex]
    label_comb['text'] = curLetter
    list_letter.select_set(curIndex)

def prevLetter(eve=None):
    global  curIndex, list_letter
    list_letter.select_clear(curIndex)
    curIndex -= 1
    updateLabel()

def nexttLetter(eve=None):
    global  curIndex, list_letter
    list_letter.select_clear(curIndex)
    curIndex += 1
    updateLabel()



def saveLetter(eve=None, imageStatus=None):
    global cavas_label, curIndex, frame_listAll, frame_Choice 

    curLetter = all_letter_list[curIndex]

    x=root.winfo_rootx() + frame_listAll.winfo_width()
    y=root.winfo_rooty() + frame_button.winfo_height() + frame_button_move.winfo_height()

    y_0 = y + canvas_width//2 - font_size
    y_1 = y + canvas_width//2 + font_size
    x_0 = x + padX 
    x_1 = x + canvas_width - padX

    # bBox = (x, y, x1, y1)
    bBox = (x_0, y_0, x_1, y_1)

    # print(bBox)

    if imageStatus.lower() == 'rejected' or imageStatus.lower() == 'r':
        imagePath = f"{rejectedImageDir}/{curLetter}.{imageExt}"
    elif imageStatus.lower() == 'accepted' or imageStatus.lower() == 'a':
        imagePath = f"{acceptedImageDir}/{curLetter}.{imageExt}"
    else:
        imagePath = f"{curDir}/outputImage/{curLetter}.{imageExt}"
    imagePath = imagePath.replace("\\", "/")
    

    if os.path.isfile(imagePath):
        os.remove(imagePath)
    ss = ImageGrab.grab(bbox=bBox)

    ss.save(imagePath)
    # print(ss, "saved")


def updateCord(eve=None):
    global label_ends
    x=eve.x
    y=eve.y

    # print(x, y)
    label_ends['text'] = f" [ {x} : {y} ]"


def showListMenu(eve=None):
    menu_list_click = Menu()


def listDoubleCLick(eve=None):
    global curIndex
    (curIndex, ) =  list_letter.curselection()
    updateLabel()
    # print(curIndex)


def listAcpRightCLick(eve=None):
    print('listAcpRightCLick')


def listRejRightCLick(eve=None):
    print('listRejRightCLick')


def updateListRej(eve=None):
    global rejected_letter_list, list_reject

    if os.path.exists(rejectedFilePath) == False:
        with open(rejectedFilePath, 'w', encoding='utf-8') as wf:
            wf.writelines('')
        wf.close()
    
    print('updating Reject List')
    with open(rejectedFilePath, 'r', encoding='utf-8') as rf:
        lines = rf.readlines()

    for line in lines:
        rejected_letter_list.append(line.strip())
        rejected_letter_dict[line.strip()] = all_letter_dict[line.strip()]
        list_reject.insert(END, line.strip())

    tempRejList = list(list_reject.get(0, END))
    TempfileList = os.listdir(f'{rejectedImageDir}')
    for fil in TempfileList:
        fn =  fil.split('.')[0]
        if fn not in tempRejList:
            os.remove(f"{rejectedImageDir}/{fil}")
    

def updateListAcp(eve=None):
    global accepted_letter_list, list_accept
    print('updating Accept List')

    if os.path.exists(acceptedFilePath) == False:
        with open(acceptedFilePath, 'w', encoding='utf-8') as wf:
            wf.writelines('')
        wf.close()

    with open(acceptedFilePath, 'r', encoding='utf-8') as rf:
        lines = rf.readlines()

    for line in lines:
        accepted_letter_list.append(line.strip())
        accepted_letter_dict[line.strip()] = all_letter_dict[line.strip()]
        list_accept.insert(END, line.strip())
    
    tempAcpList = list(list_accept.get(0, END))
    TempfileList = os.listdir(f'{acceptedImageDir}')
    for fil in TempfileList:
        fn =  fil.split('.')[0]
        if fn not in tempAcpList:
            os.remove(f"{acceptedImageDir}/{fil}")


def saveAllLetter(eve=None):
    global list_reject, list_accept, acceptedFilePath, rejectedFilePath,\
        rejected_letter_dict, accepted_letter_dict

    with open(acceptedFilePath, 'w', encoding='utf-8') as wf:
        wf.writelines('\n'.join(list(list_accept.get(0, END))))
    wf.close()

    with open(acceptedJSONPath, 'w', encoding='utf-8') as jo:
        json.dump(accepted_letter_dict, jo)
    jo.close()

    with open(rejectedFilePath, 'w', encoding='utf-8') as wf:
        wf.writelines('\n'.join(list(list_reject.get(0, END))))
    wf.close()

    with open(rejectedJSOnPath, 'w', encoding='utf-8') as jo:
        json.dump(rejected_letter_dict, jo)
    jo.close()

    print("Saved")






# highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=0, borderwidth=0
frame_root = Frame(root, bg=color_root_bg, \
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=0, borderwidth=0)
frame_root.pack(expand=True, fill="both")



frame_listAll = Frame(frame_root, bg=color_all_bg, \
    highlightbackground=color_all_bg, highlightcolor=color_all_bg, highlightthickness=0, border=0, borderwidth=0)
frame_listAll.pack(padx=3, pady=5, expand=True, fill="y", side=LEFT)
scrollY_listAll = Scrollbar(frame_listAll, orient=VERTICAL)
list_letter = Listbox(frame_listAll, bg=color_all_bg, fg=color_all_fg, font=font_shutonni, height=list_height, width=list_width, yscrollcommand=scrollY_listAll.set, \
    highlightbackground=color_all_bg, highlightcolor=color_all_bg, highlightthickness=0, border=0, borderwidth=0)
scrollY_listAll.config(command=list_letter.yview)
scrollY_listAll.pack(padx=0, pady=0, expand=False, side=RIGHT, fill="y")
list_letter.pack(padx=0, pady=0, expand=False, fill="y", side=LEFT)


frame_Label = Frame(frame_root, bg=color_lab_bg, \
    highlightbackground=color_lab_bg, highlightcolor=color_lab_bg, highlightthickness=0, border=0, borderwidth=0)
frame_Label.pack(padx=0, pady=0, expand=True, fill="both", side=LEFT)


frame_button = Frame(frame_Label, bg=color_lab_bg, \
    highlightbackground=color_lab_bg, highlightcolor=color_lab_bg, highlightthickness=0, border=0, borderwidth=0)
frame_button.pack(padx=0, pady=0, expand=False, fill="x") 
button_reject = Button(frame_button, bg=color_rej_bg, fg=color_rej_fg, font=font_button, command=rejectLetter,\
    highlightbackground=color_rej_bg, highlightcolor=color_rej_bg, highlightthickness=0, border=0, borderwidth=0)
button_reject['text'] = "Reject".upper()
button_reject.pack(padx=3, pady=5, expand=True, fill="x", side=LEFT)
button_accept = Button(frame_button, bg=color_acp_bg, fg=color_acp_fg, font=font_button, command=acceptLetter,\
    highlightbackground=color_acp_bg, highlightcolor=color_acp_bg, highlightthickness=0, border=0, borderwidth=0)
button_accept['text'] = "Accept".upper()
button_accept.pack(padx=3, pady=5, expand=True, fill="x", side=LEFT)

frame_button_move = Frame(frame_Label, bg=color_root_bg, \
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=0, borderwidth=0)
frame_button_move.pack(padx=0, pady=0, expand=False, fill="x") 
button_prev = Button(frame_button_move, bg=color_root_bg, fg=color_root_fg, font=font_button, command=prevLetter,\
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=0, borderwidth=0)
button_prev['text'] = "<<<".upper()
button_prev.pack(padx=3, pady=5, expand=True, fill="x", side=LEFT)
button_save = Button(frame_button_move, bg=color_root_bg, fg=color_root_fg, font=font_button, command=saveLetter,\
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=2, borderwidth=2)
button_save['text'] = "Save".upper()
button_save.pack(padx=3, pady=5, expand=True, fill="x", side=LEFT)
button_next = Button(frame_button_move, bg=color_root_bg, fg=color_root_fg, font=font_button, command=nexttLetter,\
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=0, borderwidth=0)
button_next['text'] = ">>>".upper()
button_next.pack(padx=3, pady=5, expand=True, fill="x", side=LEFT)



cavas_label = Canvas(frame_Label, bg = 'White', width=canvas_width, height=canvas_height, \
    highlightbackground='White', highlightcolor='White', highlightthickness=0, border=0, borderwidth=0)
label_comb = Label(cavas_label, bg='White', fg='Black', font=font_shutonni_label,\
    highlightbackground='White', highlightcolor='White', highlightthickness=0, border=0, borderwidth=0)
label_comb.pack(padx=0, pady=0, expand=True, fill="both") 

cavas_label.create_window(canvas_width//2, canvas_width//2, window=label_comb)
cavas_label.pack(padx=0, pady=0, expand=True, fill="both")

updateLabel()


frame_Choice = Frame(frame_root, bg=color_root_bg, \
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=2, border=2, borderwidth=2)
frame_Choice.pack(padx=0, pady=0, expand=True, fill="both", side=LEFT)




frame_listRej = Frame(frame_Choice, bg=color_rej_bg, \
    highlightbackground=color_rej_bg, highlightcolor=color_rej_bg, highlightthickness=0, border=0, borderwidth=0)
frame_listRej.pack(padx=3, pady=5, expand=True, fill="y")
scrollY_listRej = Scrollbar(frame_listRej, orient=VERTICAL)
list_reject = Listbox(frame_listRej, bg=color_rej_bg, fg=color_rej_fg, font=font_shutonni,  height=list_height//2, width=list_width, \
    yscrollcommand=scrollY_listRej.set,highlightbackground=color_rej_bg, highlightcolor=color_rej_bg, highlightthickness=0, border=0, borderwidth=0)
scrollY_listRej.config(command=list_reject.yview)
scrollY_listRej.pack(padx=0, pady=0, expand=False, side=RIGHT, fill="y")
list_reject.pack(padx=0, pady=0, expand=True, fill="y", side=LEFT)

button_accept_all = Button(frame_Choice, bg=color_root_bg, fg=color_root_fg, font=font_button, command=saveAllLetter,\
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=2, borderwidth=2)
button_accept_all['text'] = "Save All".upper()
button_accept_all.pack(padx=3, pady=5, expand=True, fill="x")

frame_ListAcp = Frame(frame_Choice, bg=color_acp_bg, \
    highlightbackground=color_acp_bg, highlightcolor=color_acp_bg, highlightthickness=0, border=0, borderwidth=0)
frame_ListAcp.pack(padx=3, pady=5, expand=True, fill="y")
scrollY_listAcp = Scrollbar(frame_ListAcp, orient=VERTICAL)
list_accept = Listbox(frame_ListAcp, bg=color_acp_bg, fg=color_acp_fg, font=font_shutonni, height=list_height//2, width=list_width, \
    yscrollcommand=scrollY_listAcp.set, highlightbackground=color_acp_bg, highlightcolor=color_acp_bg, highlightthickness=0, border=0, borderwidth=0)
scrollY_listAcp.config(command=list_accept.yview)
scrollY_listAcp.pack(padx=0, pady=0, expand=False, side=RIGHT, fill="y")
list_accept.pack(padx=0, pady=0, expand=True, fill="y", side=LEFT)


frame_ends = Frame(root, bg=color_root_bg, \
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=0, borderwidth=0)
frame_ends.pack(expand=False, fill="x", padx=0, pady=3)
label_ends = Label(frame_ends, bg=color_root_bg, fg=color_root_fg, \
    highlightbackground=color_root_bg, highlightcolor=color_root_bg, highlightthickness=0, border=0, borderwidth=0)
frame_ends.pack(expand=False, fill="x", padx=0, pady=3)
label_ends.pack(padx=0, pady=0, expand=True, fill="x")

updateListAcp()
updateListRej()

for ind, letter in enumerate(all_letter_list):
    list_letter.insert(ind, letter)
    if str(letter).strip() in accepted_letter_list:
        list_letter.itemconfig(ind,{'bg': color_acp_bg, 'fg': color_acp_fg})
    if str(letter).strip() in rejected_letter_list:
        list_letter.itemconfig(ind,{'bg': color_rej_bg, 'fg' : color_rej_fg})


root.bind("<Right>", nexttLetter)
root.bind("<Left>", prevLetter)
root.bind("<Return>", acceptLetter)
root.bind("<Delete>", rejectLetter)
root.bind("<Motion>", updateCord)
cavas_label.bind("<Motion>", updateCord)

list_letter.bind("<Double-Button-1>", listDoubleCLick)
list_accept.bind("<Button-3>", listAcpRightCLick)
list_reject.bind("<Button-3>", listRejRightCLick)



root.mainloop()