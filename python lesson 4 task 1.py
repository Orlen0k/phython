# ДЗ 1
# 1) Создать список случайных чисел от -10, до 10 на num * 2 элементов. num вводим с клавиатуры.
# 2) Вывести все числа меньше 0 и делящиеся на 3
# 3) Сказать кол-во элементов 5 и 3
# 4) Вывести разницу между кол-вом максимальных и минимальных значений
# 5) Сделать копию списка. Равзернуть и упорядочить список список
# 6) Удалить половину элементов списка
# 7) Очистить список
import random

# 1) Создать список случайных чисел от -10, до 10 на num * 2 элементов. num вводим с клавиатуры.

num = int(input('Введите num: '))
spisok = []
for i in range(num * 2):
    spisok.append(random.randint(-10, 10))
print(spisok)
# 2) Вывести все числа меньше 0 и делящиеся на 3
for x in spisok:
    if x < 0 and x % 3 ==0:
        print(x)
# 3) Сказать кол-во элементов 5 и 3
count = 0
for x in spisok:
    if x > 5 and x > 3:
        count += 1
print(count)
# 4) Вывести разницу между кол-вом максимальных и минимальных значений
print(f'Максимальное значение {max(spisok)}')

print(f'Минимальное значение {min(spisok)}')

print(f'Разница между максимальным и минимальным значением  {max(spisok) - min(spisok)}')

# 5) Сделать копию списка. Равзернуть и упорядочить список список
s1 = spisok.copy()
print(s1)

s1.reverse()
print(s1)
s1.sort()
print(s1)

# 6) Удалить половину элементов списка
del s1[: len(s1)//2]
print(s1)

# 7) Очистить список
s1.clear()
print(s1)







