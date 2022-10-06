# Урок 11. Jupyter Notebook и несколько слов об аналитике
# 1) Ввести с клавиатуры N и M
# Создать 2 таблицы данных в NumPy размера NxM - одну заполнить вручную, а вторую случайными числами.
# Найти сумму элементов всех массивов,
# Найти самый большой элемент массивов и самый маленький.
#

#

import sympy as sp
import numpy as np
import math
import random
import pandas as pd
import matplotlib.pyplot as plt
# сделали график
# fruits = ['apple', 'peach', 'orange', 'banana', 'lime']
# counts = [15, 26, 32, 29, 35]
# plt.bar(fruits, counts)
# # plt.bar(counts, fruits)
# plt.title('Fruits!')
# plt.xlabel('fruit')
# plt.ylabel('Count')
# plt.show()
# 1) Ввести с клавиатуры N и M
# Создать 2 таблицы данных в NumPy размера NxM - одну заполнить вручную, а вторую случайными числами.
# Найти сумму элементов всех массивов,
# # Найти самый большой элемент массивов и самый маленький.
n = int(input('Введите первое число: '))
m = int(input('Введите первое число: '))
table = np.random.randint(0, 100, (n, m))
print(table)


# 2) Создать таблицу данных в pandas - заполнить
# Добавить новый столбец.
d = [{'city': 'Moscow', 'code': 111, 'price': 1000, 'send': 0},
     {'city': 'Moscow', 'code': 222, 'price': 1500, 'send': 0},
     {'city': 'Moscow', 'code': 333, 'price': 2000, 'send': 0},
     {'city': 'Stavropol', 'code': 444, 'price': 3000, 'send': 1},
     {'city': 'Stavropol', 'code': 555, 'price': 2000, 'send': 2}]

frame = pd.DataFrame(d)
# cумму кодов нашли
ixmac = frame.groupby('city')['code'].sum()
# сортировка по цене
ixmac = frame.sort_values(by='price')
# фильтр по признакам
ixmac = frame.query('price < 3000 & send == 0')
print(ixmac)
#
# объединение таблиц

df_1 = pd.DataFrame([['nina', 56, 34, 28],
                     ['ann', 21, 39, 75],
                     ['ira', 57, 36, 44]],
                    columns=['name', 'январь','февраль', 'март'])

df_2 = pd.DataFrame([['bob', 11, 42, 18],
                     ['sonya', 79, 31, 52]],
                    columns=['name', 'январь','февраль', 'март'])

df = pd.concat([df_1, df_2])
# порядок в индексах
df.reset_index(drop=True, inplace=True)
print(df_1)
print()
print(df_2)
print()
print(df)
df["Апрель"] = [10, 20, 30, 40, 50]
print(df)


# 3) Построить график y = 1\x
# Настроить внешний вид таблицы
import matplotlib.pyplot as plt
import numpy as np
y = np.linspace(-40, 40, 10000)
x = 1 / np.abs(y)
plt.figure(1)
plt.title('График функции y  = 1 / x')
plt.ylabel('Ось y')
plt.xlabel('Ось x')
plt.grid()
plt.axis([-10, 10, -4, 10])
plt.plot(x, y)
plt.show()


