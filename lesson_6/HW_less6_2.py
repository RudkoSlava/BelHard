def count_char(my_string):
    my_string = my_string.replace(' ','')
    dict_count = {}
    for i in my_string:
        if dict_count.get(i, None):
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    return dict_count

STR_VAL = 'python is the fastest-growing major programming language'
print(count_char(STR_VAL))


