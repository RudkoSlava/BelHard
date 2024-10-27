from collections import Counter

python_zen = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

line_count = len(python_zen.split('\n'))
print(line_count)

split_zen = python_zen.split()
is_zen = Counter(split_zen)
and_zen = Counter(split_zen)
or_zen = Counter(split_zen)

element_is = 'is'
element_and = 'and'
element_or = 'or'

count_is = is_zen[element_is]
count_and = is_zen[element_and]
count_or = is_zen[element_or]

dict_zen = {element_is:count_is, element_and:count_and, element_or:count_or}
print(dict_zen)

list_zen = list({python_zen})
string_zen = " ".join(list_zen)
new_zen = string_zen.replace("is", "is not")
print(new_zen)