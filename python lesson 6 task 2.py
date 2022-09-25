# 2.1 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# Пример:
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
#
# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension

lst = [1, 2, 3, 5, 1, 5, 3, 10]

used = set()
unique = [x for x in lst if x not in used and (used.add(x) or True)]
print(unique)

from collections import Counter
counter = Counter(lst)

unique = list(counter)
print(unique)


single = [x for x,n in counter.items() if n==1]
print(single)


unique = [x for i, x in enumerate(lst) if i == lst.index(x)]
print(unique)
