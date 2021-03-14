import os
from os.path import supports_unicode_filenames
import shutil
from tabulate import tabulate

#All Directories with MC saves
dirs =  ("C:\\Users\\Jannis\\AppData\\Local\\MultiMC\\instances", "C:\\Users\\Jannis\\AppData\Roaming\\.minecraft", "C:\\Users\\Jannis\\Desktop\\mc_files\\globalSaves\\")

class save:
    def __init__(self, name, root) -> None:
        self.name = name
        self.root = root
        self.table = [name, root]

    def __str__(self):
        return self.name


def getAllSaves(directory):
    saves = []
    for roots, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            #get all "saves" directories in dir
            if subdirectory == "saves":
                for subroot, subsubdir, subfile in os.walk(os.path.join(roots, subdirectory)):
                    #get path of all saves
                    saveroot = subroot
                    slashsave = saveroot.find("saves\\")
                    name = saveroot[slashsave+6:]
                    if slashsave > 0:
                        cutoffstring = saveroot[slashsave+6:]
                        #check if it is a subdir
                        if cutoffstring.find("\\") < 0:
                            n = save(name, saveroot)
                            saves.append(n)
    return saves


def getValidInput(message, stop):
    while True:
        userdec = input(message + "(0;%i)" %(stop-1))
        try:
            userdec = int(userdec)
        except ValueError:
            print("This is not a valid Input")
            continue
        return userdec


def getNiceList(list):
    nice_list = []
    for n in list:
        nice_list.append(n.table)
    return nice_list


def getDecisions(duplicates:list, saves:list):
    return_Queue = []
    delete_Queue = []
    for duplicate in duplicates:
        times = 0
        option_Queue = []
        for thissave in saves:
            if duplicate == thissave.name:
                option_Queue.append(thissave)
                times += 1
                print(thissave.table)
        userdec = getValidInput("Wich version do you want to keep? ", times)
        return_Queue.append(option_Queue.pop(int(userdec)))
        for option in option_Queue:
            delete_Queue.append(option)
    return [return_Queue, delete_Queue]


def saveToGlobalSaves(directories):
    #get all saves
    all_saves = []
    for dir in directories:
        some_saves = getAllSaves(dir)
        for saves in some_saves:
            all_saves.append(saves)

    #get all names
    all_names = []
    for saves in all_saves:
        all_names.append(saves.name)

    #get all duplicates
    bad_singles = []
    double_names = []
    for names in all_names:
        if names not in bad_singles:
            bad_singles.append(names)
        else:
            double_names.append(names)

    #get a good singles list
    singles = []
    for saves in all_saves:
        if saves.name not in double_names:
            singles.append(saves)

    #Printing All Saves
    print(tabulate(getNiceList(all_saves)))

    #get The Copy list
    copy_list = []
    decs = getDecisions(double_names, all_saves)
    for n in decs[0]:
        copy_list.append(n)
    for single in singles:
        copy_list.append(single)

    #get the Delete list
    delete_list = decs[1]

    #Printing Result
    print("\nCopy list:\n" + tabulate(getNiceList(copy_list)))
    print("\nDelete list:\n" + tabulate(getNiceList(delete_list)))


if __name__ == "__main__":
    saveToGlobalSaves(dirs)