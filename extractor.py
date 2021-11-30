#!/usr/bin/env python3

import os
import shutil
import sys

def root(drive_path):
    root = os.listdir(drive_path)

    if not len(root):
        print("The drive is empty.")
    else:
        for file in root:
            print(file)

def search(path):
    if os.path.exists(path):
        return True
    else:
        return False

def getItemSize(filepath):
    filesize = 0
    if os.path.isdir(filepath):
        for path, dirs, files in os.walk(filepath):
            for f in files:
                fp = os.path.join(path, f)
                filesize += os.path.getsize(fp)
    else:
        filesize = os.path.getsize(filepath)

    if filesize < 1024:
        print("Item size: " + str(filesize) + " Bytes")
    elif filesize >= 1024 and filesize < 1024**2:
        print("Item size: " + "{:.2f}".format(filesize / 1024) + " KiB")
    else:
        print("Item size: " + "{:.2f}".format(filesize / 1024**2) + "MiB")

def delete(drive_path, filename):
    filepath = os.path.join(drive_path, filename)
    
    if not search(filepath):
        print("File '" + filename + "' doesn't exist!")
        sys.exit()
        
    getItemSize(filepath)
    
    option = str(input("\033[1m" + ":: Are you sure you want to delete '" + filename + "' ? [Y/n] " + "\033[0m"))

    if option == "Y" or option == "y":
        if os.path.isdir(filepath):
            shutil.rmtree(filepath)
        else:
            os.remove(filepath)

        print("\nThe item has been erased.")
    elif option == "N" or option == "n":
        sys.exit()
    else:
        print("Unknown command!")