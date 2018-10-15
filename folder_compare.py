'''
rsync -av --exclude='*.exe' --exclude='*.com' --exclude='*.dll' --exclude='*.msi' --exclude='*.jar' --exclude='*.class' /media/ubuntu/Acer/ /media/ubuntu/Seagate\ Backup\ Plus\ Drive/Angel\ PC/

mount -t ntfs-3g /dev/sdb3 /media/ubuntu/Acer
'''

import os
import fnmatch
from filecmp import cmp 
from shutil import copyfile
from os.path import splitext, join, exists, isdir, islink
import pprint

folder1 = "/media/ubuntu/Acer"
folder2 = "/media/ubuntu/Seagate Backup Plus Drive/Angel PC"

extensions_to_ignore = [
    ".class", # java class
    ".com", # executable
    ".crash", # apple crash log
    ".dll", # executable
    ".exe", # executable
    ".ips", # patch file for games
    ".jar", # java lib
    ".log", # log
    ".msi", # installer
    ".msp", # windows patch installer
    ".mui", # multilingual interface
    ".otf", # open type font
    ".sdl", # service description, used by microsoft prior to wsdl
    ".sys", # system files on windows
    ".ttf", # true type font
]

pathes_to_ignore = [
    "/media/ubuntu/Acer/DrFoneCache", # fully reviewed
    "/media/ubuntu/Acer/inetpub", # fully reviewed
    "/media/ubuntu/Acer/Intel", #fully reviewed 
    "/media/ubuntu/Acer/OEM", # fully reviewed
    "/media/ubuntu/Acer/Program Files", # fully reviewed, pf.txt
    "/media/ubuntu/Acer/Program Files (x86)", # fully reviwed, pf86.txt
    "/media/ubuntu/Acer/ProgramData", # generating pdata.txt
    "/media/ubuntu/Acer/RemotePrograms", # fully reviewed
    "/media/ubuntu/Acer/System Volume Information", # fully reviewed
    "/media/ubuntu/Acer/Users/Ange/AppData",
    "/media/ubuntu/Acer/Users/Ange/Saved Games", # fully reviewed
    "/media/ubuntu/Acer/WINDOWS", # fully reviwed, windows.txt
]

def ignored_extension(file):
    name, ext = splitext(file)
    return ext.lower() in extensions_to_ignore

def ignored_path(a_path):
    for path in pathes_to_ignore:
        if a_path.startswith(path):
            return True
    return False

def copy(file1, file2):
    try:
        copyfile(file1, file2)
        print("COPIED")
    except:
        print("FAIL to copy")

for root1, dir1, files1 in os.walk(folder1):
    if islink(root1):
        print("===")        
        print("IGNORE LINK: " + root1)
        continue

    dir1[:] = [d for d in dir1 if not join(root1, d) in pathes_to_ignore]
    print("+++")
    print("D: " + root1)
    pprint.pprint(dir1)  
         
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
                try:
                    if cmp(file1, file2, shallow=True):
                        print("F1 == F2")
                    else:
                        print("F1 != F2")
                        copy(file1, file2)
                except:
                    print("FAIL to cmp")
            else:            
                print("F2 MISSING")
                copy(file1, file2)
        else:
            print("IGNORE")
'''
ep 1
    https://www.youtube.com/watch?v=ksZ07DSIXhE
    there was a female taxi driver who was on the same ninja show as the trans guy - one of the often    
    noodle soup
ep 2
    https://www.youtube.com/watch?v=EcPvptkWMts
    the comedian and his teacher, they fight and get together again    
    american hotdog
ep 3
    https://www.youtube.com/watch?v=i9UW3Q0muao
    the girl always made stweater for someone does not like her, but finally a guy liked her
    think cut pork steak
ep 4
    https://www.youtube.com/watch?v=XXX833O2NMo
    the physics professor and the koream girl
    egg wrapped rice
ep 5
    https://www.youtube.com/watch?v=3AGaDUL545k&list=PLDfVaLcddwHI2OYXezMiyJIrpUbPeVYAg&index=6
    a boy and his father, who is master of gambling
    tofu on top of rice
ep 6
    https://www.youtube.com/watch?v=ZooHmT97QxY&index=10&list=PLDfVaLcddwHI2OYXezMiyJIrpUbPeVYAg
    the owner of the veg stall, his mother and the nurse who loves him    
    ume pickle
ep 7
    https://www.youtube.com/watch?v=PulUHBREVZI&list=PLDfVaLcddwHI2OYXezMiyJIrpUbPeVYAg
    the daughter of the shoe store boss and her nephew
ep 8
    https://www.youtube.com/watch?v=zeTZGnjNceU&index=18&list=PLDfVaLcddwHI2OYXezMiyJIrpUbPeVYAg
    the guy making adult video and his first - the wife of the boss    
    fried huaishan
ep 9 
    https://www.youtube.com/watch?v=o7jmIgEAxQI
    the lawyer found his brother
ep 10
    https://www.youtube.com/watch?v=oUf6hgbxUnU
    the guy win horse bet and the newyear eve everyone together

hotpot
    change to low before go sleep
    turn off tmr morning
    try some
    let Y try
Angel form
    check online version
    make sure check all docs
check program files folder
    generatign list right now
what did I eat today
    breakfast
        1 yogurt
        2 dinner roll
        1 chocolate
    lunch
        some egg/spinach/turkey dish
        1 banana
    dinner
        some dishes Angel bought

'''
