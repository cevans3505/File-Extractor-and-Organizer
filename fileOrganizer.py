#!/usr/bin/env python3

"""
Created by Distilled
Contact: distilled@protonmail.com
31 August 2017
Version 0.2
"""

# Simple Python script to extract all files from
# subdirectories into the parent directory.

import shutil
import os 

# What file extensions do you want to preserve? (Wildcard character: *)
# Example 1 (Extract specific file types):  keepExts = [".png", ".txt", ".mp*"]
# Example 2 (Extract all file types):       keepExts = [".*"]
keepExts = [".txt", ".zip"]

# Define destination directory (absolute filepath)
# Default (if blank): parent dir
destDir = 'C:\\Users\cevan\\Desktop\\Test Py Dir\\destDir'

# Get absolute dir path where script executed
cwd = os.getcwd()

# Create empty arrays to contain log info for output to console at end of script
movedFiles = []
deletedDirectories = []

if destDir == "":
    destDir = cwd
else:
    destDir = destDir

# Generator that walks DOWN the folder tree
walker = os.walk(cwd)

# 'data' returns a 3 index tuple (dirpath, dirnames, filenames)
for data in walker:
    # Get files contained within sub dir(s)
    for files in data[2]:
        if os.path.splitext(files)[1] in keepExts:
            try:
                # Move file(s) to destDir
                shutil.move(data[0] + os.sep + files, destDir)
                movedFiles.append(files)

            except shutil.Error:
                continue

print("Successfully moved the following file(s) into " + cwd + ":\n")
for i in movedFiles:
    print(i)




















#exitFunc = input("Press 'Enter' key to exit.")
exit()