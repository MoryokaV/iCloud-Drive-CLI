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
        
    print("Upload finished!")

def download(file, filename, local):
    if os.path.isfile(file):
        shutil.copy(file, local)
    else:
        local += "/" + filename
        shutil.copytree(file, local)

    print("Download finished!")

    extractor.delete(file, filename)
