#!/usr/bin/env python3

import shutil
import extractor
import os

def upload(drive, file, filename):
    if os.path.isfile(file):
        shutil.copy(file, drive)
    else:
        drive += "/" + filename
        extractor.displayItemSize(file)
        shutil.copytree(file, drive)
        
    print("Uploaded finished!")

def download(file, filename, local):
    if os.path.isfile(file):
        shutil.copy(file, local)
    else:
        local += "/" + filename

        extractor.displayItemSize(file)
        shutil.copytree(file, local)

    print("Download finished!")

    extractor.delete(file, filename)
