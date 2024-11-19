import re

def check_login(login):
    check = r'^[A-Za-z0-9_-]{5,20}$'
    if re.match(check,login):
        return 'Логин подходит'
    else:
        return 'Логин неверен'

logins = input('Введите желаемый логин: ')
print(check_login(logins))

