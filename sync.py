#!/usr/bin/env python3

import sys
import os
import shutil
import platform
import getpass

global drive_path
script_path = sys.argv[0]

def initialize():
    global drive_path
    OS = platform.system()

    if OS == "Darwin":
        username = getpass.getuser()
        drive_path = "/Users/" + username + "/Library/Mobile Documents/com~apple~CloudDocs"
          
        if not os.path.exists(drive_path):
            print("iCloud Drive is not enabled in System Preferences.")
            sys.exit()
    elif OS == "Windows":
        drive_path = ""
    else:
        print("Your OS is not compatible with this script.")
        sys.exit()
    
    drive_path += "/Transfer"
    if not os.path.exists(drive_path):
        os.mkdir(drive_path)
        print("init: 'Transfer' directory has been created in your iCloud Drive.\n")

def helpPopup():
    print("[###] iCloud Drive CLI - Code by Vlaviano\n")
    print("download + filename | -> download specified file/folder from cloud")
    print("upload + filename | -> upload specified file/folder to cloud")
    print("root | -> list the root of the cloud directory")
    print("delete + filename | -> delete specified file/folder from cloud")

    sys.exit()

def selector():
    cmd = str(sys.argv[1])

    if cmd == "help":
        helpPopup()
    elif cmd == "upload":
        print("upload")
    elif cmd == "download":
        print("download")
    elif cmd == "root":
        print("root")
    elif cmd == "delete":
        print("delete")
    else:
        print("Unknown command. Type 'help' for more details.")

if __name__ == '__main__':
    initialize()
    selector()
