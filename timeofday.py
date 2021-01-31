print("Wie viel Ihr ist es (in h)")
zeit = (int(input())) % 24
if zeit < 8:
    print("schlafen!")

elif zeit < 12:
    print("Frühstück!")

elif zeit < 14:
    print("Mittagessen!")

elif zeit < 18:
    print("Kaffee und Kuchen!")

elif zeit < 20:
    print("Abendessen!")

else:
    print("schlafen!")
