import os
from os.path import supports_unicode_filenames
import shutil
from tabulate import tabulate

#All Directories with MC saves
dirs =  ("C:\\Users\\Jannis\\AppData\\Local\\MultiMC\\instances", "C:\\Users\\Jannis\\AppData\Roaming\\.minecraft", "C:\\Users\\Jannis\\Desktop\\mc_files\\globalSaves\\")

def getAllSaves(directory):
    allRoots = []
    for roots, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            #get all "saves" dirs in dir
            if subdirectory == "saves":
                for subroot, subsubdir, subfile in os.walk(os.path.join(roots, subdirectory)):
                    # get path of all saves
                    saveroot = subroot
                    slashsave = saveroot.find("saves\\")
                    name = saveroot[slashsave+6:]
                    if slashsave > 0:
                        cutoffstring = saveroot[slashsave+6:]
                        #check if it is a subdir
                        if cutoffstring.find("\\") < 0:
                            allRoots.append((name, saveroot))
    return allRoots


def getValidInput(stop):
    while True:
        userdec = input("Wich version do you want to keep? (0;%i)" %(stop-1))
        try:
            userdec = int(userdec)
        except ValueError:
            print("This is not a valid Input")
            continue
        return userdec


def getDecisions(duplicates, saves):
    returnQueue = []

    for duplicate in duplicates:
        times = 0
        optionQueue = []
        for save in saves:
            if duplicate[0] == save[0]:
                optionQueue.append(save)
                times += 1
                print(save)
        userdec = getValidInput(times)
        returnQueue.append(optionQueue[int(userdec)])
    return returnQueue



if __name__ == "__main__":
    saves = []
    names = []
    duplicates = []
    singles = []

    #Get all saves
    for dir in dirs:
        saves += getAllSaves(dir)

    #Get a list with all save names
    for name, root in saves:
        names.append(name)

    #get the names of the duplicates
    for n in names:
        if n not in singles:
            singles.append(n)
        elif n in singles:
            duplicates.append([n])

    if True:
        print("all saves")
        print(tabulate(saves))
        #print("\nsingles")
        #print((singles))
        #print("\nduplicates")
        #print((duplicates))

    print(getDecisions(duplicates, saves))