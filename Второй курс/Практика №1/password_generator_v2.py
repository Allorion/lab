#!/usr/bin/python
#by Allori  https://github.com/Allorion/
from itertools import permutations, combinations

#Ввод необходимых значений и выбор режима работы программы
aphabet = input('Введите алфавит для генирации пароля:')
repeat = input('Введите 1 если требуется пароль без повторения символов\nВведите 2 если требуется пароль с повторением символов\n')
choice = input('Введите 1 если хотите получить пароль длиной равной длине алфавита\nВведите 2 если хотите получить пароль длиной на 2 символа короче длины алфавита\n')
#Создаем переменную для подсчета количества паролей
quantity = 0

#Проверям возможность повторения символов и выполняем действия с алфавитом
if repeat == '1':
    aphabet = "".join(set(aphabet))
elif repeat == '2':
    aphabet = aphabet
else:
    print('Вы ввели не верный вариант')

#Режимы работы программы с длиной алфавита
if choice == '1':
    number = len(aphabet)
elif choice == '2':
    number = len(aphabet)-2
else:
    print('Вы ввели не верный вариант')

#Тело программы для генерации пароля
for i in permutations(aphabet, number):
    quantity += 1
    a = ''.join(i)
    print(f'Пароль {quantity}) {a}')
print(f'Количество паролей:{quantity}')
