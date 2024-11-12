def yes_or_no(num):
    n = len(num)
    for i in range(n):
        if num[i] in num[0:i]:
            print('Yes')
        else:
            print('No')
    return n

list_num = list(map(int, input('Введите числа через пробел:').split()))
yes_or_no(list_num)

