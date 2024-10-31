#text = input('Введите предложение: ')

#if len(text) > 10:
#    print ('Long')
#elif len(text) < 10:
#    print('Short')
#else:
#    print('Bug')

###########################################

#num = int(input('Введите число: '))

#if num == 0:
#    print(f'Число {num} не является четным или нечетным')
#elif num %2 == 0:
#    print ('Это число ' + str(num) + ' четное')
#else:
#    print('Это число ' + str(num) + ' нечетное')

############################################

#rating = input('Введите Вашу оценку: ')

#if  int(rating) >= 0:
#    if  85 <= int(rating) <= 100:
#        print ('Отлично')
#    elif 60 <= int(rating) <= 84:
#        print('Хорошо')
#    elif 40 <= int(rating) <= 59:
#        print('Удовлетворительно')
#    else:
#        print('Неудовлетворительно')
#else:
#    print("Введите корректную оценку")

######################################

#while True:
#    a = input('Введите слово: ')
#    if a.lower() == "stop":
#        break
#    else: print(a)

###########################################

#total = 0
#number = 1

#while True:
#    total += number
#    number = number + 1
#    print(total)
#    if number == 100:
#        break

#############################################

#index = [1, 2, 3, 'str', 5]

#for i in index:
#    if type(i) == str:
#        print(i + '!')
#    else:
#        print(i * 10)

##############################################

#for i in range(0, 101):
#    if i %7 == 0:
#        print(i)

#############################################
for i in range(1,101):
    if i %7 == 0 and i %5 == 0:
        print(i)
        break