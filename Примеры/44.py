def reversed(func):
    def wrapper(message):
        return func(message)[::-1]

    return wrapper


@reversed
def hello(name):
    return f'Hi {name}'


print(hello('user'))
