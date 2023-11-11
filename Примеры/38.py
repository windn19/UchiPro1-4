def add(x):
    def func(y):
        return x + y

    return func


add5 = add(5)
print(add5(3))  # 8
print(add5(0))  # 5
print(add5(-1))  # 4

add7 = add(7)
print(add7(3))  # 10
print(add7(-2))  # 5
