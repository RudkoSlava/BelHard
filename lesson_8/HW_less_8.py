from abc import ABC, abstractmethod

class Transport(ABC):
    brand : str
    model : str
    issue_year : int
    color : str
    mileage : int

    def __init__(self, brand, model, issue_year, color):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color
        self.mileage = 0

    @abstractmethod
    def move(self,num_km):
        pass

    def move(self, num_km):
        if num_km >= 0:
            self.mileage = self.mileage + num_km
        else:
            raise ValueError('Расстояние должно быть положительным числом')

class Car(Transport):
    engine_type: str
    def __init__(self, brand, model, issue_year, color, engine_type):
        super().__init__(brand, model, issue_year, color)
        self.engine_type = engine_type

    def move(self,num_km):
        super().move(num_km)
        return f'{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {num_km} километров.'

class Airplane(Transport):
    lifting_capacity : int
    def __init__(self, brand, model, issue_year, color, lifting_capacity):
        super().__init__(brand, model, issue_year, color)
        self.lifting_capacity = lifting_capacity

    def move(self,num_km):
        super().move(num_km)
        return f'{self.brand} {self.model} ({self.color} - {self.issue_year}) пролетел {num_km} километров.'

Car1 = Transport(brand = "BMW", model = "A6", issue_year = 2015, color = "Черный")
Car1.move(1)
print(Car1.mileage)
Car1.move(15)
print(Car1.mileage)
# Car1.move(-5)
# print(Car1.mileage)

Car2 = Car(brand = "BMW", model = "A6", issue_year = 2015, color = "Черный", engine_type = "Бинзин")
message_car = Car2.move(20)
print(message_car)

Airplane1 = Airplane(brand = "Boing", model = "747", issue_year = 2015, color = "Белый", lifting_capacity = 300)
message_air = Airplane1.move(200)
print(message_air)
