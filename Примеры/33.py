x = 'global'


def f():
    x = 'enclosing'

    def g():
        nonlocal x
        x = 'change enclosing'
        print(x)

    g()
    print(x)  # change enclosing


f()
print(x)
