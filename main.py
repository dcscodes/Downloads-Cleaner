# import os package for python
import send2trash
import os
from os import listdir

# get folder path from user
folderPath = input("Please specify the folder you would like to clean;\n")
fileType = input("Now specify the file type you want to delete. EXAMPLE: .png\n")

for fileName in listdir(folderPath):
    if fileName.endswith(fileType):
        send2trash.send2trash(folderPath + fileName)
        print(fileName + " has been moved to your Trash Bin!")