#!/usr/bin/env python3

import os
import shutil
import sys

def root(drive_path):
    root = os.listdir(drive_path)

    maxx = len(max(root))

    if not len(root):
        print("The drive is empty.")
    else:
        for file in root:
            print(file + " " * (maxx - len(file)) + "  |  " + str(displayItemSize(drive_path + "/" + file)))

def search(path, filename):
    if not os.path.exists(path):
        print("ERROR: Incorrect file name '" + filename + "'")
        sys.exit()

def displayItemSize(filepath):
    filesize = 0
    if os.path.isdir(filepath):
        for path, dirs, files in os.walk(filepath):
            for f in files:
                fp = os.path.join(path, f)
                filesize += os.path.getsize(fp)
    else:
        filesize = os.path.getsize(filepath)

    if filesize < 1024:
        return(str(filesize) + " Bytes")
    elif filesize >= 1024 and filesize < 1024**2:
        return("{:.2f}".format(filesize / 1024) + " KiB")
    else:
        return("{:.2f}".format(filesize / 1024**2) + " MiB")

def delete(filepath, filename):
    print("")
    option = str(input("\033[1m" + ":: Do you want to delete '" + filename + "' ? [Y/n] " + "\033[0m"))

    if option == "Y" or option == "y":
        if os.path.isdir(filepath):
            shutil.rmtree(filepath)
        else:
            os.remove(filepath)

        print("The item has been erased.")
    elif option == "N" or option == "n":
        sys.exit()
    else:
        print("Unknown command!")
