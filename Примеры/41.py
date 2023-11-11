def decorator_func(func):
    def wrapper():
        print('Начало')
        func()
        print('Конец')

    return wrapper


def test():
    print('Тест')


test = decorator_func(test)
test()
