# Урок 7. Python: от простого к практике
# Создать телефонный справочник используя файлы, модули и исключения

base = {}

with open('text.txt', mode="r", encoding="utf-8") as f:
    for line in f:
        key, val = line.strip().split(':')
        base[key] = val.split()

for key,val in base.items():
    print(f"{key} : {' '.join(val)}")
