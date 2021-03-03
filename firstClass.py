class FirstClass:
    int = 42
    string = "imastring"

    def __init__(self, newchar="a"):
        self.char = newchar


    def do_something(self, neuezahl=43):
        self.int = neuezahl
        return self.int

instance = FirstClass("z")
print(instance.int)
print(instance.do_something(1))
print(instance.int)

print(instance.char)