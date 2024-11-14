class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        return (f'{self.name} что то говорит ')

class Dog(Animal):

    def voice(self):
        return (f'{self.name} говорит ГАВ!')

class Bird(Animal):

    def fly(self):
        return (f'{self.name} летит на ЮГ')

    def voice(self):
        return (f'{self.name} говорит ЧИРИК!')

class Insect(Dog, Bird):

    def voice(self):
        return (f'{self.name} говорит ЖЖЖЖЖ!')

    def jump(self):
        return (f'{self.name} прыгает')

Dog1 = Dog("Собака", 20)
Bird1 = Bird("Сокол", 3)
Insect1 = Insect("Комар", 0.1)
print(Dog1.voice())
print(Bird1.fly())
print(Bird1.voice())
print(Insect1.voice())
print(Insect1.fly())
print(Insect1.jump())

