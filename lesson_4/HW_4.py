spisok_1 =  [2, 3, 4, 5, 6, 7]
spisok_2 = ['March', 'April', 'May' , 'June', 'Jule', 'August']

task_1_1 = int(input("Введите новое первое число: "))
spisok_1.insert(0, task_1_1)
task_1_2 = int(input("Введите новое последнее число: "))
spisok_1.append(task_1_2)

task_1_3 = input("Введите новый первый месяц: ")
spisok_2.insert(0, task_1_3)
task_1_4 = input("Введите новый последний месяц: ")
spisok_2.append(task_1_4)

print(spisok_1)
print(spisok_2)

spisok_1.extend(spisok_2)
print(spisok_1)