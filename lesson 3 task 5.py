# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num):
    """Function to return jokes. num (int) - count of jokes"""
    joke_ls=[]
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        joke_ls.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_ls

print(get_jokes(1))
print(get_jokes(2))

def get_jokes_adv(num, repeats=True):
    joke_ls = []

    if not repeats:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                joke_ls.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')

            else:
                for i in range(num):
                    cur_nouns = random.choice(nouns)
                    cur_adverbs = random.choice(adverbs)
                    cur_adjectives = random.choice(adjectives)
                    joke_ls.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
            return joke_ls
print(get_jokes_adv(4, False))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, False))