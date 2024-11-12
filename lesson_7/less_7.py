# class Animal:
#     animal_type : str
#     title_zoo = 'Zoo'
#     animal_type_count = 1
#
#     def __init__(self, animal_type):
#         self.animal_type = animal_type
#
#     @classmethod
#     def animal_count(cls):
#         cls.animal_type_count +=1
#         print('Добавлено животное')
#
#
# tigger = Animal('Тигр')
# print(tigger.animal_type, tigger.title_zoo)
#
# print(tigger.animal_type_count)
# Animal.animal_count()
# print(tigger.animal_type_count)

################################################

class Calculate:

    @staticmethod
    def add_num(a, b):
        return a+b

    @staticmethod
    def sub_num(a, b):
        if a < b:
            print('а должно быть больше b')
        else:
            return a-b

    @staticmethod
    def mul_num(a, b):
        return a*b

    @staticmethod
    def del_num(a, b):
        if b == 0:
            print('На ноль делить нельзя')
        else:
            return a/b

print(Calculate.add_num(2,3))
print(Calculate.del_num(2, 0))
print(Calculate.sub_num(3,4))


