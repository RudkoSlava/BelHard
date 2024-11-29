# file = open("test", 'r')
# content = file.read()
# print(content)
# file.close()

##################################
#
# file = open("test", 'r')
# lines = file.readlines()
# for line in lines:
#     print(line)
# file.close()

##################################
#
# file = open("test2", 'w', encoding="UTF-8")
# file.write("Что-то")
# file.close()

##################################

# with open("test2", 'r', encoding="UTF-8") as file:
#     content = file.read()
#     print(content)

##################################

# import json
#
# data = {"name": "Slava", "age": 29}
#
# with open("class_work.json",'w') as file:
#     json.dump(data, file)

##################################
#import json

# with open("class_work.json", "r") as file:
#     dict_json_data = json.load(file)
# print(dict_json_data)

##################################
#
# from pydantic import BaseModel
#
# class User(BaseModel):
#     username: str
#     age: int
#
# valid_user_data = {"username": "Slava", "age": 29}
# valid_user = User(**valid_user_data)
#
# print(f' Good query: {valid_user}')

##################################

# from pydantic import BaseModel
#
# class BaseUser(BaseModel):
#     username: str
#
# class User(BaseUser):
#     age: int
#
# class Profile(User):
#     skills: list
#
# valid_user_data = {"username": "Slava", "age": 29, "skills": ['Python']}
#
# valid_user = Profile(**valid_user_data)

##################################

#from pydantic import BaseModel

# class Product(BaseModel):
#     name: str
#     price: float
#     quantity: int
# def add_product(name, price, quantity):
#     return Product(name=name, price=price, quantity=quantity)
#
# product = {"name": "Milk", "price": 2, "qiantity": 25}
# print(add_product("Milk", 2, 25))

##################################

# from pydantic import BaseModel, ValidationError
# import json

# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#
# def test(name, age, email):
#     return User(name=name, age=age, email=email)
#
# person = User(name="Slava", age=28, email="1234567890cdz@gmail.com")
#
# json_data = person.json()
#
# with open("Persons.json", "w") as json_file:
#     json_file.write(json_data)
#
# print("Данные успешно добавлены в 'Persons.json'")

##################################

# from pydantic import BaseModel, ValidationError
# import json

# class User(BaseModel):
#     name: str
#     age: int
#     email: str
# def test():
#     user_input = {
#         "name": input('Введите имя: '),
#         "age": input('Введите возраст: '),
#         "email": input('Введите email: ')
#     }
#
#     try:
#         user = User(**user_input)
#         with open("Persons.json", 'w', encoding="UTF-8") as file:
#             json.dump(user.dict(), file, indent=4)
#         print("Данные успешно сохранены.")
#     except ValidationError as e:
#         print("Ошибка валидации данных.", e)
#
# test()

##################################

import csv

data = [
    ['name', 'age'],
    ['Bob', 32],
    ['Alex', 35]
]

with open('data.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',')
    for row in data:
        csvwriter.writerow(row)