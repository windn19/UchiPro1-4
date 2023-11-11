def hello():
    message = 'Привет'

    def func():
        print(message)

    return func


f = hello()
f()
