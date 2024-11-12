#def summ_num(num):
#    if num > 10:
#        num = num + 5
#        return num
#    else:
#        num = 3 - num
#        return num

#number = int(input('Введите число: '))
#print(summ_num(number))

##########################################

#def reverse_string(string):
#    string = string[::-1]
#    string = ''.join(reversed(string))
#    return string
#
#fin_string = input("Введите строку: ")
#print(reverse_string(fin_string))

##########################################

# animal = {
#     "type" : 'Лев',
#     "count" : 40
# }

# def add_animal(total):
#     animal["count"] += total
#     return animal
#
# def delete_animal(total):
#     animal["count"] -= total
#     return animal
#
# def refresh(type, count):
#     animal['type'] = type
#     animal['count'] = count
#     return animal
#
# print(animal)
#
# add_animal(25)
# print(animal)
#
# delete_animal(40)
# print(animal)
#
# refresh("Зебра", 24)
# print(animal)

#####################################

#spisok = list(filter(lambda x: x > 5, [1,15, 25, 35,2, 4, 3]))
#print(spisok)

####################################

def user(name, age, company="Python", experience =1):
    user = {
        name : age,
        company : experience
    }
    return user

people = user('Слава', 28)
print(people)