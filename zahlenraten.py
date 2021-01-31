import random

zahl = random.randint(0, 20)

print("Rate die Zahl!")
n = 1

while True:
    print("das ist dein " + str(n) + ". Versuch")
    zufall = (int(input()))
    if n >= 5:
        print("du hast zu viele Züge gebraucht!")
        break
    elif  zufall == zahl:
        print("erraten!")
        break
    elif zufall > zahl :
        print("Zu Hoch!")
    else:
        print("Zu Niedrig!")
    n +=  1

    
    