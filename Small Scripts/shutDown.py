import os
import time
from datetime import datetime



def doShutDown():
    print("done")
    os.system("shutdown /s /t 1")
    exit()
while True:
    allnames = ""
    for file in os.listdir("C:\\Users\\Jannis\\Downloads\\"):
        allnames += file
    if allnames.find(".part") < 0:
        doShutDown()
    else:
        print("still Downloading    " + str(datetime.now(tz=None)))
    time.sleep(10)       

