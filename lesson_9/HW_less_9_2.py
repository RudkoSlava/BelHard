import re
def check_phone(phone):
    check = r'^\+375\((29|33|44|25)\)\d{3}-\d{2}-\d{2}$'

    if len(phone) != 17:
        print("Неверная длина номера. Номер должен быть формата +375(код оператора)ххх-хх-хх.")
        return

    if not re.match(check, phone):
        if phone[0:4] != "+375":
            print("Номер должен начинаться с +375.")
            return
        elif phone[4:8] not in ("(29)", "(33)", "(44)", "(25)"):
            print("код оператора должен быть 29, 33, 44, 25 и взят в ().")
            return
        elif not phone[8:11].isdigit():
            print("Номер не должен содержать букв.")
            return
        elif phone[11] != "-":
            print("Проверьте наличие '-'. Номер должен быть формата +375(код оператора)ххх-хх-хх.")
            return
        elif not phone[12:14].isdigit():
            print("Номер не должен содержать букв.")
            return
        elif phone[14] != "-":
            print("Проверьте наличие '-'. Номер должен быть формата +375(код оператора)ххх-хх-хх.")
            return
        elif not phone[15:17].isdigit():
            print("Номер не должен содержать букв.")
            return
        else:
            print("Номер телефона не соответствует ожидаемому формату.")
    else:
        print("Номер телефона верен!")

Phone_number = input("Введите проверяемый номер: ")
check_phone(Phone_number)

# import re
# def check_phone(phone):
#     check = r'^\+375\((29|33|44|25)\)\d{3}-\d{2}-\d{2}$'
#     if re.match(check, phone):
#         print("Номер телефона верен")
#     else:
#         print("Проверьте формат номера. Номер должен быть формата +375(код оператора)ххх-хх-хх")
#
# Phone_number = input("Введите проверяемый номер: ")
# check_phone(Phone_number)