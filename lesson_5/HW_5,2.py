rubles = input('Введите количество рублей: ')
kopeck = input('Введите количество копеек: ')
#rubles_1 = ['р', 'у', 'б', 'л']
#kopeck_1 = ['к', 'о', 'п', 'е']

#ending = {1:'ь', 2:'я', 3:'я', 4:'я', 5:'ей', 6:'ей', 7:'ей', 8:'ей', 9:'ей', 10:'ей',
#          11:'ей', 12:'ей', 13:'ей', 14:'ей', 15:'ей', 16:'ей', 17:'ей', 18:'ей', 19:'ей',
#          20:'ей', 30:'ей', 40:'ей', 50:'ей', 60:'ей', 70:'ей', 80:'ей', 90:'ей' }

#for a, b in ending.items():
#    if rubles == a:
#        str(rubles_1.append(b))
#        print(str(rubles) + ' ' + ''.join(rubles_1))
#    else:
#        print("Проверьте введеные данные")
#        break

if rubles[-2:] in ('11', '12', '13', '14','15', '16','17', '18', '19', '20'):
    rub_text = ' рублей '
elif rubles[-1] == '1':
    rub_text = ' рубль '
elif rubles[-1] in ('2', '3', '4'):
    rub_text =  ' рубля '
else:
    rub_text =  ' рублей '

if kopeck[-2:] in ('11', '12', '13', '14','15', '16','17', '18', '19', '20'):
    kop_text = ' копеек'
elif kopeck[-1] == '1':
    kop_text = ' копейка'
elif kopeck[-1] in ('2', '3', '4'):
    kop_text = ' копейки'
elif int(kopeck) > 100:
    print('Столько копеек не существует')
else:
    kop_text = ' копеек'

print(rubles + rub_text + kopeck + kop_text)