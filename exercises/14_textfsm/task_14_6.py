# -*- coding: utf-8 -*-
'''
Задание 14.6

Это задание похоже на задание 14.5, но в этом задании подключения надо выполнять параллельно с помощью потоков. Для параллельного подключения использовать модуль concurrent.futures.

Для этого надо использовать функцию connect_ssh (в задании) и функцию parse_command_dynamic из упражнения 14.4.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функции connect_ssh и parse_command_dynamic
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
 * но надо иметь в виду, какие аргументы ожидают готовые функции, которые используются
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей (то есть, тот вывод, который был получен из функции parse_command_dynamic)

Для функции conn_processes создан файл devices.yaml, в котором находятся параметры подключения к устройствам.

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

'''

import yaml
from pprint import pprint

from netmiko import ConnectHandler


test_command = "sh ip int br"
devices = yaml.load(open('devices.yaml'))


def connect_ssh(device_dict, command):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)

        print('Connection to device {}'.format(device_dict['ip']))
    return {device_dict['ip']: result}


