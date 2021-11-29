#!/usr/bin/env python3

import os

def root(drive_path):
    root = os.listdir(drive_path)

    if not len(root):
        print("The drive is empty.")
    else:
        for file in root:
            print(file)
