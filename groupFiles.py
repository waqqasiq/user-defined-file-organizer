# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:15:06 2019

@author: waqqas.iqbal
"""
import os
import shutil
import pandas as pd

path = os.getcwd()
names = os.listdir(path)


df = pd.read_csv('fileFolder.csv')

folder_name = []
file_name = []
for f in df['FolderName']:
    folder_name.append(f)

for f in df['FileName']:
    file_name.append(f)

folder_name_set = list(set(folder_name))   

######## CURRENT TIME #################
from datetime import datetime
from pytz import timezone
def date_time(zone='Asia/Dhaka'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    year = other_zone_time.strftime('%y')
    month = other_zone_time.strftime('%m')
    day = other_zone_time.strftime('%d')
    hour = other_zone_time.strftime('%H')
    minute = other_zone_time.strftime('%M')
    if int(hour)>12:
        hour = int(hour) - 12
        minute = str(minute)+"pm"
    else:
        minute = str(minute)+"am"
    return str(day)+"-"+str(month)+"-"+str(year)+"-"+str(hour)+"-"+str(minute)
######################################
    
date_time = date_time()  


file = open("logfile.txt","w") 
folder_created = []
files_moved = []


j=0 #Count of files moved    
k=0 #count of folder created 

for files in names:
    if ((files=="fileFolder.csv") | (files=="groupFiles.py") | (files=="logfile.txt")):
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
            if not os.path.exists(path+"\\"+folder_name[i]):
                os.makedirs(path+"\\"+folder_name[i])
                folder_created.append(folder_name[i])
                k+=1
            shutil.move(path+"\\"+files, path+"\\"+folder_name[i]+"\\"+files)
            files_moved.append(files)
            j+=1
    
    
print("Folder created: ", k)   
print("Files moved: ", j)
print("Check the logfile.txt for more details.")


file.write("Folder created: \n")
for f in folder_created:
    file.write(f + "\n")

file.write("\n")

file.write("Files moved: \n")
for f in files_moved:
    file.write(f + "\n")

file.write("\n") 
file.write("Folder created: "+ str(k) + "\n")  
file.write("Files moved: "+ str(j) + "\n")   
file.write("Timstamp (d-m-y-H-M) : "+date_time)  
 
file.close() 
