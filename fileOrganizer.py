#!/usr/bin/env python3

"""
Created by Distilled
Contact: distilled@protonmail.com
3 September 2017
Version 0.4
"""

# Python script to extract all files from sub-directories into a user defined location.

############################# BEGIN USER CONFIGURATION #########################################

# What file extensions do you want to preserve? (Wildcard character: *)
# Example 1 (Extract specific file types):  keepExts = [".png", ".txt", ".mp*"]
# Example 2 (Extract all file types):       keepExts = [".*"]
keepExts = [".*"]

# Define destination directory (absolute dir path)
# Default (if blank): parent dir
# Example (Windows):    destDir = 'C:\\Users\administrator\\Desktop\\Extracted'
# Example (Unix/Linux): destDir = '/home/distilled/Desktop/Extracted'
destDir = ''

# What directories do you want to omit from extraction & deletion routines? (absolute dir path)
# Note: The destination directory defined above (destDir) is already included
# Example (Windows):    skipDirs = ['C:\\Users\administrator\\Desktop\\dir1', 'C:\\Users\administrator\\Desktop\\dir2']
# Example (Unix/Linux): skipDirs = ['/home/distilled/Desktop/dir1', '/home/distilled/Desktop/dir2']
skipDirs = []

############################ END USER CONFIGURATION ############################################


import shutil
import os

# Get absolute dir path where script executed
rootDir = os.getcwd()

# Create empty arrays to contain log info for output to console at end of script
movedFiles = []
deletedDirectories = []

# Set destination directory to default value (parent dir) unless otherwise defined in user configuation section
if destDir == '':
    destDir = rootDir
else:
    destDir = destDir

# Add destination directory to list of skipped directories
skipDirs.append(destDir)

# Get basename of each dir in skipDirs (for use in directory deletion routine)
skipDirsBasename = []
for i in skipDirs:
    skipDirsBasename.append(os.path.basename(i))

# 1st directory walk DOWN the directory tree - File extraction routine
walker = os.walk(rootDir)

# 'data' returns a 3 index tuple (dirpath, dirnames, filenames)
for roots, dirs, files in walker:
    # Check to see if user wants to skip current dir
    if roots not in skipDirs:
        for file in files:
            # Check to see if file ext matches any ext listed in 'keepExts'
            if os.path.splitext(file)[1] in keepExts:
                try:
                    shutil.move(roots + os.sep + file, destDir)
                    movedFiles.append(file)

                except shutil.Error:
                    continue

# 2nd directory walk DOWN the directory tree - Directory deletion routine
walker = os.walk(rootDir)

# 'data' returns a 3 index tuple (dirpath, dirnames, filenames)
for roots, dirs, files in walker:
    for curDir in dirs:
        if curDir not in skipDirsBasename:
            try:
                shutil.rmtree(rootDir + os.sep + curDir)
                deletedDirectories.append(curDir)
				
            except shutil.Error:
                continue

print("\nSuccessfully moved the following file(s) into " + destDir + ":")
for i in movedFiles:
    print(i)

print("\nThe following sub-directories (including all files remaining within) were deleted:")
for i in deletedDirectories:
    print(i)

input("Press 'Enter' key to exit.")
exit()
