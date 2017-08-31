#!/usr/bin/env python3

"""
Created by Distilled
Contact: distilled@protonmail.com
31 August 2017
Version 0.1
"""

# Simple Python script to extract all files from
# subdirectories into the parent directory.

import shutil
import os 

# Get absolute dir path where script executed
cwd = os.getcwd()

# Generator that walks DOWN the folder tree
walker = os.walk(cwd)

# 'data' returns a 3 index tuple (dirpath, dirnames, filenames)
for data in walker:
    # Get files contained within sub dir(s)
    for files in data[2]:
        try:
            # Move file(s) to parent dir
            shutil.move(data[0] + os.sep + files, cwd)
        except shutil.Error:
            continue

exitFunc = input("Press 'Enter' key to exit.")
exit()
