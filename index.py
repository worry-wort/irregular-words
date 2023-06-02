from pandas import read_excel
from random import randint

words = read_excel('words.xlsx', 'Лист1')
'''
Лист1 вписувати не обов'язково, якщо у нас всього одна робоча таблиця
'''
val = list(words)
listed_words = list(words[val] for val in val)
'''
записуємо все в змінну, але то ще не список,
бо list() криво працює з ітерованими об'єктами
'''

for form in range(len(listed_words)):
    listed_words[form] = list(listed_words[form])
'''
от тепер нарешті ми маємо список списків
тут вкладені чотири списки в такій послідовності:
перша форма, друга, форма, третя форма, укр переклад
'''

for lst in listed_words:
    for wrd in range(len(lst)):
        for lttr in lst[wrd]:
            if lttr == ',':
                lst[wrd] = lst[wrd].split(',')

'''
не знаю чи це буде потрібно, але цей кусок
написаний для випадків, коли у слова декілька значень
і він розділяє його на список з двох змінних
так як попередньо вони йдуть одним цілим
'''
num = int(input('к-ть слів: '))

def words_check(listed, num):
    wor = None
    right, wrong = 0, 0
    while wor != 'stop':
        a = randint(0, 2)
        c = a + 1
        b = randint(0, num)
        wor = input(f'{listed[3][b]} {c} форма: \n')
        if wor == listed[a][b]:
            right += 1
        elif wor != listed[a][b] and wor != 'stop':
            print('правильно буде ', listed[a][b])
            wrong += 1
    print(right, wrong)
    pass

words_check(listed_words, num)

'''
while True:
    ans = input('напиши для почтаку "start", щоб закінчити та побачити результат напиши "stop": \n')
    if ans == 'start' or ans == 'stop':
        break
'''
