# -*- coding: utf-8 -*-
import sys
import yaml
import threading
from queue import Queue
from pprint import pprint
import logging

from netmiko import ConnectHandler


COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))


#logging setup
FORMAT = '%(asctime)-15s [%(levelname)s] (%(threadName)-10s) %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def connect_ssh(device_dict, command, queue):
    logging.info('Connection to device {}'.format(device_dict['ip']))
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        #Добавляем словарь в очередь
        queue.put({device_dict['ip']: result})


def conn_threads(function, devices, command):
    threads = []
    q = Queue()

    for device in devices:
        # Передаем очередь как аргумент, функции
        th = threading.Thread(target=function, args=(device, command, q))
        th.start()
        threads.append(th)

    logging.info('All threads started')

    for th in threads:
        th.join()

    results = []
    # Берем результаты из очереди и добавляем их в список results
    for t in threads:
        results.append(q.get())

    return results

pprint(conn_threads(connect_ssh, devices['routers'], COMMAND))

