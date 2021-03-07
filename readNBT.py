from nbt import nbt
from tabulate import tabulate
#path = "C:\\Users\\Jannis\\Desktop\\mc files\\globalSaves\\ReBu Server"
path = "level.dat"


nbtfile = nbt.NBTFile(path, "rb")
print(tabulate(nbtfile))
