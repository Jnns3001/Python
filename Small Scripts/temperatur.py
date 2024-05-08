def CinF(C):
    F = (C*9/5)+32
    return F

def CinK(C):
    while True:
        try:
            C = float(C)
            K = C + 273.15
            if K < 0:
                return "impossible"
            else:
                return K
        except ValueError:
            print("this was not a Number")


def getTemp():
    while True:
        C = input("Gib mir eine Temperatur in Celsius ")
        try:
            C = float(C)
            return C
        except ValueError:
            return "Das war keine Zahl"


if __name__ == "__main__":
    c = getTemp()
    print(CinK(c))
