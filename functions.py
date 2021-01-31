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