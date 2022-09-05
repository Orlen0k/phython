# number = int(input("Введите число обозначающее день недели: "))
# new_number = int(input("Введите число от 1 до 7: "))
# if number == 6 or number == 7:
#     print("Выходной день")
# elif number < 6 or number <= 1:
#     print("Рабочий день")
# while number > 7 or number < 1:
#     print(new_number int(input("Введите число от 1 до 7: ")))
#     if new_number == 6 or new_number == 7:
#         print("Выходной день")
#     elif new_number < 6 or new_number <= 1:
#         print("Рабочий день")
#
#         # if number == 6 or number == 7:
#         #     print("Выходной день")
#         # else:
#         #     print("Рабочий день")
#
#     # if number > 7 or number < 1:
#     #     print(int(input("Введите число от 1 до 7: ")))
#     # elif number == 6 or number == 7:
#     #     print("Выходной день")
#     # else:
#     #     print("Рабочий день")
#
# # elif number == 6 or number == 7:
# #     print("Выходной день")
# # else:
# #     print("Рабочий день")

#
# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
#
#         *Пример:*
#
# #         - 6 -> да
#         - 7 -> да
#         - 1 -> нет

number = int(input('Введите число обозначающее день недели: '))
if number > 7 or number < 1:
    print('Введите число от 1 до 7')
elif number == 6 or number == 7:
    print("Выходной день!")
else:
    print("Рабочий день")