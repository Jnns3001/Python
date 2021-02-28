import os
import shutil

#All Directories with MC saves
dirs =  ("C:\\Users\\Jannis.Laptop\\AppData\\Local\\MultiMC\\instances", "C:\\Users\\Jannis.Laptop\\AppData\Roaming\\.minecraft")

def getAllSaves(directory="C:\\Users\\Jannis.Laptop\\AppData\\"):
    allRoots = []
    for roots, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            #get all "saves" dirs
            if subdirectory == "saves":
                for subroot, subsubdir, subfile in os.walk(os.path.join(roots, subdirectory)):
                    # get path of all saves
                    saveroot = subroot
                    slashsave = saveroot.find("saves\\")
                    name = saveroot[slashsave+6:]
                    if slashsave > 0:
                        cutoffstring = saveroot[slashsave+6:]
                        #check if there is a subdir in the save
                        if cutoffstring.find("\\") < 0:
                            allRoots.append((saveroot, name))
    return allRoots

saveroots = []
names = []
for dir in dirs:
    saveroots += getAllSaves(dir)
for root, name in saveroots:
    print(name)
    names.append(name)
print(names)

duplicates = []
singles = []
for n in names:
    if n not in singles:
        singles.append(n)
    elif n in singles:
        duplicates.append(n)

print(singles, duplicates)
