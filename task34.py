# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку 
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять 
# из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы 
# отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом 
# все не в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# пара-ра-рам рам-пам-папам па-ра-па-дама
# Вывод:
# Парам пам-пам

def count_vowels(phrase):
    vowels_list = ['а', 'о', 'у', 'ы', 'э', 'я', 'ё', 'ю', 'и', 'е']
    for i in range(len(phrase)):
        phrase[i] = len(list(filter(lambda x: x in vowels_list, phrase[i])))
    return phrase

def check_rythm(poetry_list):
    phrases_list = count_vowels(poetry_list.split())
    return len(list(filter(lambda x: x - phrases_list[0], phrases_list))) == 0

poem = input("Input Vinni's poem: ")
if check_rythm(poem):
    print('Парам пам-пам')
else:
    print('Пам парам')

