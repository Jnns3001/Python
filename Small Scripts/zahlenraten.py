import random
import math

def getvalidNumber():
    while True:
        guess = input("Give me a number!")
        try:
            guess = int(guess)
        except ValueError:
            print("That was not a number!")
            continue
        return guess


def guessingGame(x=1,y=20):
    number = random.randint(x, y)
    print("Guess a number between "+ str(x) + " and " + str(y) + "!")
    n = 1
    maxtries = int(math.log2(y-x))+1
    print(maxtries)

    while n <=maxtries:
        print(str(n) + ". try")

        guess = getvalidNumber()

        if  guess == number:
            print("you got it!")
            return True
        elif guess < number :
            print("too small!")
        else:
            print("too big!")
        n +=  1

    return False

        
if __name__ == "__main__":
    guessingGame()