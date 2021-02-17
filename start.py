import functions as f

def onlineMode(replacement):
    index = text.find("online-mode=") + 12
    length = text.find("level-seed=") - index
    return f.replace(text, index, length, replacement)


def map(replacement):
    index = text.find("level-name=") + 11
    length = text.find("view-distance=") - index
    return f.replace(text, index, length, replacement)


if __name__ == "__main__":
    path = "C:\\Users\\Jannis.Laptop\\Desktop\\mc files\\Server\\Server 1.16.5 paper\\server.properties"
    file = open(path)
    global text
    text = file.read()
    file.close()

    if input("Standard Settings? (1/0)") == "0":
        if input("OnlineMode? (1/0)") == "1":
            text = onlineMode("True\n")
        else:
            text = onlineMode("False\n")

        if input("Standard Map? (1/0)") == "1":
            text = map("Rebu Server\n")
        else:
            text = map(input("map name?")+ "\n")

    print (text)

    file = open(path,"w")
    file.write(text)
    file.close