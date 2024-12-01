import json
from pydantic import BaseModel

data = [
    {
        "id": 1,
        "name": "Slava",
        "age": 28,
        "interests": ["youtube", "games"],
        "salary": 2000.0
    },
    {
        "id": 2,
        "name": "Vladimir",
        "age": 28,
        "interests": ["reading", "games"],
        "salary": 1600.0
    },
    {
        "id": 3,
        "name": "Maxim",
        "age": 30,
        "interests": ["song", "telephone"],
        "salary": 1700.0
    },
    {
        "id": 4,
        "name": "Katerina",
        "age": 27,
        "interests": ["IT", "programing"],
        "salary": 8500.0
    },
    {
        "id": 5,
        "name": "Luba",
        "age": 54,
        "interests": ["cinema", "learning"],
        "salary": 1500.0
    }
]


# with open("HW_10.json", 'w') as json_file:
#     json.dump(data, json_file, indent=4)


class Users(BaseModel):
    id: int
    name: str
    age: int
    interests: list = None
    salary: float


class OldUser(BaseModel):
    id: int
    name: str


class AllUser(BaseModel):
    id: int
    name: str
    age: int
    interests: list = None
    salary: float


DATA_FILE = "HW_10.json"


def read_users():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def add_user(name: str, age: int, interests: list, salary: float):
    users = read_users()
    max_id = max(user['id'] for user in users) if users else 0
    new_id = max_id + 1

    user = Users(id=new_id, name=name, age=age, interests=interests, salary=salary)
    users.append(user.dict())

    with open(DATA_FILE, 'w', encoding="UTF-8") as f:
        json.dump(users, f, indent=4)


def read_user():
    users = read_users()
    print("Все пользователи: ")
    for user in users:
        old_users = OldUser(id=user['id'], name=user['name'])
        print(old_users)


def check_user(user: AllUser):
    user_id = user.id
    users = read_users()
    for record in users:
        if record['id'] == user_id:
            print("Данные о пользователе:")
            print(record)
            return
    print("Пользователь с таким ID не найден.")


name = input("Введите имя нового сотрудника: ")

if not name:
    print("Имя пустое, новый сотрудник не был добавлен.")
else:
    age = int(input("Введите возраст нового сотрудника: "))
    interests = input("Введите интересы нового сотрудника через запятую: ").split(",")
    salary = float(input("Введите зарплату нового сотрудника: "))

    add_user(name=name, age=age, interests=interests, salary=salary)
    print("Новый сотрудник добавлен")

read_user()
user_id = int(input("Введите ID пользователя: "))
search_user = AllUser(id=user_id, name="", age=0, interests=[], salary=0.0)
check_user(search_user)
