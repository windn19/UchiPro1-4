# Напиши функции для регистрации и авторизации пользователя: registration(user, password) и authorization(user, password).
#
# Функция registration() добавляет пользователя и ничего не выводит. Если при регистрации пользователя логин уже был
# зарегистрирован ранее, то это значит, что для данного пользователя необходимо обновить пароль.
#
# Функция authorization() выводит:
#     • «Доступ разрешен», если пара пользователь пароль верная
#     • «Неверный пароль», если пароль не верный
#     • «Пользователь не найден», если нет такого пользователя.
#
# Входные данные:
# Вводится одно целое число n — количество строк, на следующих n строках вводятся команды в формате:
#     • registration userpassword через 1 пробел, команда должна вызывать функцию registration() с параметрами user и password.
#     • authorization user password через 1 пробел, команда должна вызывать функцию authorization() с параметрами user и password.
#
# Выходные данные:
# Выводятся строки.
#
# Пример работы программы:
# 6
# registration('user', '123456')
# authorization('user', '123456')
# authorization('user', '12345678')
# authorization('admin', '12345678')
# registration('user', '12345678')
# authorization('user', '12345678')
# Пример вывода:
# Доступ разрешен
# Неверный пароль
# Пользователь не найден
# Доступ разрешен

# Пример ввода:
# 3
# registration user 123456
# authorization user 123
# authorization user 123456
# Пример вывода:
# Неверный пароль
# Доступ разрешен


users = {}


def registration(user, password):
    # global users
    users[user] = password


def authorization(user, password):
    if user not in users.keys():
        print('Пользователь не найден')
    elif password == users[user]:
        print('Доступ разрешён')
    else:
        print('Неверный пароль')


for i in range(int(input())):
    command = input().split()
    if command[0] == 'registration':
        registration(command[1], command[2])
    elif command[0] == 'authorization':
        authorization(command[1], command[2])
