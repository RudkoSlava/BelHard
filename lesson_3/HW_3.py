firstname = input("Введите имя: ")
lastname = input("Введите фамилию: ")
age = input("Введите возраст: ")
task_1 = f'Привет, меня зовут {firstname} {lastname}, мне {age} лет'
print(task_1)

task_2 = task_1[2]
print(task_2)

task_3 = task_1[-2]
print(task_3)

task_4 = task_1[0:5]
print(task_4)

task_5 = task_1[0:-2]
print(task_5)

some_str = "Hello, World!"
some_str = some_str.replace("World", firstname)
print(some_str)