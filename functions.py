import time


def fac(n):
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product


def rfac(n):
    if n == 1: return 1
    return n * rfac(n-1)


def fib(n):
    if n <=2 : return 1
    return fib(n-1)+fib(n-2)


def crunchForKiddies():
    for i in range(2):
        for o in range(2):
            for x in range(2):
                for y in range(2):
                    print(i,o,x,y)
                    time.sleep(0.1)


def f(L=None):
    if L is None:
        L = []
    L.append(42)
    return L


def list(stop,start=0,step=1,y=None):
    if y is None:
        y = []
    for i in range(start, stop, step):
        y.append(i)
    return y


def funk():
    print("hello world")


def funk2():
    return 42
