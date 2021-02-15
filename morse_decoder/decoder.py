def decode(message):
    pass

if __name__ == "__main__":
    encodedFile = open("morse.txt", "r")

    encodedText = encodedFile.read()

    print(encodedText)
