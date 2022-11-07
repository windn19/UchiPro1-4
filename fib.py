import time


def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)


def fib1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b


def fib2(n):
    if n in m.keys():
        return m[n]
    return fib2(n-1) + fib(n-2)




m = {0: 0, 1: 1}
for f in [fib, fib1, fib2]:
    t = time.time()
    print(f(40))
    print(time.time() - t)