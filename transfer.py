#!/usr/bin/env python3

import shutil
import extractor
import os

def upload(drive, file, filename):
    if os.path.isfile(file):
        shutil.copy(file, drive)
    else:
        drive += "/" + filename
        shutil.copytree(file, drive)
        
    print("The item has been uploaded.")

def download(file, local):
    #option = str(input("Delete item from cloud after download? [Y/n] "))
    
    if os.path.isfile(file):
        shutil.copy(file, local)
    else:
        shutil.copytree(file, local)
