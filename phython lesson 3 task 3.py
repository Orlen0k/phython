# 3) Вводим строчку и выводим разницу между
# количеством букв в верхнем и нижнем регистре.

str1 = input(": ")
count = 0
for i in (str1):
    if i == i.upper():
        count += 1
print(count)

