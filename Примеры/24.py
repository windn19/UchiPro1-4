old_string = ''


def does_something(string):
    global old_string
    if string != old_string:
        print(string)
        old_string = string


does_something('Привет')
does_something('Привет')
does_something('Пока')
