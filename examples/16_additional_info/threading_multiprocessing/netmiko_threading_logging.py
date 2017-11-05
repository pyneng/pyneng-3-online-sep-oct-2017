import sys
import yaml
import threading
import logging

from netmiko import ConnectHandler


COMMAND = sys.argv[1]
devices = yaml.load(open('devices.yaml'))


#logging setup
FORMAT = '%(asctime)-15s [%(levelname)s] (%(threadName)-10s) %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.info('Start')

def connect_ssh(device_dict, command):
    logging.info('Connection to device {}'.format(device_dict['ip']))
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info('\n'+result)


def conn_threads(function, devices, command):
    threads = []
    for device in devices:
        th = threading.Thread(target = function, args = (device, command))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


conn_threads(connect_ssh, devices['routers'], COMMAND)
