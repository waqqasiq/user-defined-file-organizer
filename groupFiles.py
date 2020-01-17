# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:28:02 2020

@author: Waqqas
"""

import os
import shutil
import pandas as pd
from tkinter import filedialog
from tkinter import *

#path = os.getcwd()
#names = os.listdir(path)

df = pd.read_csv('fileFolder.csv')

folder_name = []
file_name = []
for f in df['FolderName']:
    folder_name.append(f)

for f in df['FileName']:
    file_name.append(f)

folder_name_set = list(set(folder_name))   


root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

#print("folder selected")
#print(folder_selected)

names = os.listdir(folder_selected)
#print("names")
#print(names)

folder_created = []
files_moved = []
k=0 #count of folder created 
j=0 #Count of files moved


for files in names:
    if ((files=="fileFolder.csv") | (files=="groupFiles.py")):
        continue
    iterator = -1
    c = 0
    while(c<len(files)):
        if(files[iterator]=="."):
            break
        c+=1
        iterator-=1
    file_extension = files[iterator:]

    for i in range(len(file_name)):
        if file_extension==file_name[i]:
            if not os.path.exists(folder_selected+"\\"+folder_name[i]):
                os.makedirs(folder_selected+"\\"+folder_name[i])
                folder_created.append(folder_name[i])
                k+=1
            shutil.move(folder_selected+"\\"+files, folder_selected+"\\"+folder_name[i]+"\\"+files)
            files_moved.append(files)
            j+=1

print("Folder created:")
print(k)

print("Files moved:")
print(j)
