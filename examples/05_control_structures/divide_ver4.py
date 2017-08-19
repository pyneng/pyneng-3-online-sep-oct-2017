# -*- coding: utf-8 -*-

try:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print('Что-то пошло не так...')
else:
    print('Результат в квадрате: ', result**2)
finally:
    print('Вот и сказочке конец, а кто слушал - молодец.')

'''
Example:

$ python divide_ver4.py
Введите первое число: 10
Введите второе число: 2
Результат в квадрате:  25
Вот и сказочке конец, а кто слушал - молодец.

$ python divide_ver4.py
Введите первое число: qwerewr
Введите второе число: 3
Что-то пошло не так...
Вот и сказочке конец, а кто слушал - молодец.

$ python divide_ver4.py
Введите первое число: 4
Введите второе число: 0
Что-то пошло не так...
Вот и сказочке конец, а кто слушал - молодец.
'''
