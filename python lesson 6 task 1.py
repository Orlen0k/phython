# 1.1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
#  1-2*3 => -5;
# 1.2 Добавьте возможность использования скобок, меняющих приоритет операций.
#
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;


import re

# 2+2 => 4;
test_str = "2 + 2"
print("The original string is : " + test_str)
res = sum(map(int, re.findall(r'[+-]?\d+', test_str)))
print("The evaluated result is : " + str(res))


# 1.2 Добавьте возможность использования скобок, меняющих приоритет операций.
#
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;

actions = {
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def my_eval(expresion: str) -> str:
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))

    return expresion


exp = "(1+2)*3"
print(my_eval(exp), eval(exp))
