x = 'global'


def f():
    y = 'enclosing'

    def g():
        z = 'local'
        print(x, y, z)  # global enclosing local

    g()


f()
