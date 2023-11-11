def func(a):
    b = 4
    c = 5
    print(locals())  # {'a': 3, 'b': 4, 'c': 5}


x = 1
y = 2
func(3)
print(globals())
# {'__name__': '__main__', '__doc__': None,'__package__': None,
# ...
# 'func': <function func at 0x0000021AAAAE3E20>, 'x': 1, 'y': 2}
