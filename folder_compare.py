import os
import fnmatch
from filecmp import cmp 
from shutil import copyfile
from os.path import splitext, join, exists

folder1 = "c:/"
folder2 = "e:/cbackup/"

extensions_to_ignore = [
    ".class", #java class
    ".com", #executable
    ".dll", #executable
    ".exe", #executable
    ".jar", #java lib
    ".msi", #installer
    ".mui", # multilingual interface
]

def ignored_extension(file):
    name, ext = splitext(file)
    return ext.lower() in extensions_to_ignore

def copy(file1, file2):
    try:
        copyfile(file1, file2)
        print("COPIED")
    except Exception as e:
        print("FAIL")
        print(e)

for root1, dir1, files1 in os.walk(folder1):
    root2 = root1.replace(folder1, folder2)
    if not os.path.exists(root2):
        try:
            os.makedirs(root2)
        except:
            print("FAILED TO CREATE FOLDER: " + root2)

    for file1 in files1:
        print("===")
        file1 = join(root1, file1)
        print("F1: " + file1)
        if not ignored_extension(file1):
            file2 = file1.replace(folder1, folder2)
            print("F2: " + file2)
            if exists(file2):
                if cmp(file1, file2, shallow=True):
                    print("F1 == F2")
                else:
                    print("F1 != F2")
                    copy(file1, file2)
            else:            
                print("F2 MISSING")
                copy(file1, file2)
        else:
            print("IGNORE")