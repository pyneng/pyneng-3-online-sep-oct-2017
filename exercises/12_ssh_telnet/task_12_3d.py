# -*- coding: utf-8 -*-
'''
Задание 12.3d

Переделать функцию check_ip_addresses из задания 12.3c таким образом,
чтобы она позволяла контролировать количество параллельных проверок IP.

Для этого, необходимо добавить новый параметр limit,
со значением по умолчанию - 2.

Функция check_ip_addresses должна проверять адреса из списка
таким образом, чтобы в любой момент времени максимальное количество
параллельных проверок было равным limit.

'''

