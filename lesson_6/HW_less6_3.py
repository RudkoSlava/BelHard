def decorator_bread_up(func):
    def wrapper(*args, **kwargs):
        print("</------------\\>")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator_tomato(func):
    def wrapper(*args, **kwargs):
        print("*** помидоры ****")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator_salad(func):
    def wrapper(*args, **kwargs):
        print("~~~~ салат ~~~~~")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator_cheese(func):
    def wrapper(*args, **kwargs):
        print("^^^^^ сыр ^^^^^^")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator_onion(func):
    def wrapper(*args, **kwargs):
        print("----- лук ------")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator_beef(func):
    def wrapper(*args, **kwargs):
        print("### говядина ###")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator_chicken(func):
    def wrapper(*args, **kwargs):
        print("|||| курица ||||")
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator_bread_down(func):
    def wrapper(*args, **kwargs):
        print("<\\____________/>")
        result = func(*args, **kwargs)
        return result
    return wrapper
@decorator_bread_up
@decorator_onion
@decorator_tomato
@decorator_beef
@decorator_bread_down

def hamburger():
    return ''

print('                                                              ')
print(hamburger())

print('--------------------------чикенбургер-------------------------')
print('                                                              ')
@decorator_bread_up
@decorator_cheese
@decorator_salad
@decorator_chicken
@decorator_bread_down

def chicken_burger():
    return ''

print(chicken_burger())