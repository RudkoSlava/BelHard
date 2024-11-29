# file = open("test", 'r')
# content = file.read()
# print(content)
# file.close()
import json

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
#
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

from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    quantity: int
def add_product(name, price, quantity):
    return Product(name=name, price=price, quantity=quantity)

product = {"name": "Milk", "price": 2, "qiantity": 25}
print(add_product("Milk", 2, 25))



