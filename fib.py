import time


def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)



t = time.time()
print(fib(100))
print(time.time() - t)