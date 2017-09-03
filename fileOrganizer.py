#!/usr/bin/env python3

"""
Created by Distilled
Contact: distilled@protonmail.com
31 August 2017
Version 0.2.1
"""

# Simple Python script to extract all files from
# subdirectories into the parent directory.

import shutil
import os 

# What file extensions do you want to preserve? (Wildcard character: *)
# Example 1 (Extract specific file types):  keepExts = [".png", ".txt", ".mp*"]
# Example 2 (Extract all file types):       keepExts = [".*"]
keepExts = [""]

# Define destination directory (absolute filepath)
# Default (if blank): parent dir
destDir = ''

# Which directories do you want to omit? (absolute filepath)
skipDirs = ['']

# Get absolute dir path where script executed
cwd = os.getcwd()

# Create empty arrays to contain log info for output to console at end of script
movedFiles = []
deletedDirectories = []

if destDir == "":
    destDir = cwd
else:
    destDir = destDir

# 1st walk
walker = os.walk(cwd)

# 'data' returns a 3 index tuple (dirpath, dirnames, filenames)
for data in walker:
    # Check to see if user wants to skip current dir
    if data[0] not in skipDirs:
        for file in data[2]:
            # Check to see if file ext matches any ext listed in 'keepExts'
            if os.path.splitext(file)[1] in keepExts:
                try:
                    shutil.move(data[0] + os.sep + file, destDir)
                    movedFiles.append(file)

                except shutil.Error:
                    continue

print("\nSuccessfully moved the following file(s) into " + destDir + ":")
for i in movedFiles:
    print(i)




















#exitFunc = input("Press 'Enter' key to exit.")
exit()