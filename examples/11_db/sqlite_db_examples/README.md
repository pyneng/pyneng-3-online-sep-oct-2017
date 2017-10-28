## Примеры баз данных

* f5_clusters.sqlite - сделана из содержимого [CSV файла](https://github.com/vijayajyothi/planning/blob/master/csv_data/f5/f5_clusters.csv)
* dhcp_snooping.db - пример БД, которая используется в заданиях к разделу 
* rib_table.sqlite можно самостоятельно сделать из CSV файла rib.table.lg.ba.ptt.br-BGP.csv.gz. [Источник](https://github.com/intrig-unicamp/ALTO-as-a-Service/blob/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz)


### Импорт CSV

Для начала надо скачать CSV файл (заархивированный):
```
wget https://github.com/intrig-unicamp/ALTO-as-a-Service/raw/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz
--2017-10-28 05:15:26--  https://github.com/intrig-unicamp/ALTO-as-a-Service/raw/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz
Resolving github.com (github.com)... 192.30.253.112, 192.30.253.113
Connecting to github.com (github.com)|192.30.253.112|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://raw.githubusercontent.com/intrig-unicamp/ALTO-as-a-Service/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz [following]
--2017-10-28 05:15:27--  https://raw.githubusercontent.com/intrig-unicamp/ALTO-as-a-Service/master/IXP-PTT-BR/20141208/PTTMetro-LG-Dataset/IPv4/processed/rib.table.lg.ba.ptt.br-BGP.csv.gz
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.0.133, 151.101.64.133, 151.101.128.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.0.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6140871 (5.9M) [application/octet-stream]
Saving to: ‘rib.table.lg.ba.ptt.br-BGP.csv.gz’

rib.table.lg.ba.ptt.br-BGP.csv.gz      100%[===========================================================================>]   5.86M  6.46MB/s   in 0.9s

2017-10-28 05:15:29 (6.46 MB/s) - ‘rib.table.lg.ba.ptt.br-BGP.csv.gz’ saved [6140871/6140871]
```

> Если wget не установлен, выполните ```$ sudo apt-get install wget```

Распаковать архив:
```
$ gunzip rib.table.lg.ba.ptt.br-BGP.csv.gz
```

Теперь в каталоге появился файл rib.table.lg.ba.ptt.br-BGP.csv.


Для импорта содержимого CSV файла в БД используется sqlite3 CLI.

Создание БД rib_table.sqlite:
```
$ sqlite3 rib_table.sqlite
-- Loading resources from /home/vagrant/.sqliterc

SQLite version 3.8.7.1 2014-10-29 13:59:56
Enter ".help" for usage hints.
sqlite>
```

Для импорта надо переключить режим в csv и затем выполнить команду .import - первый аргумент имя файла, а второй - имя таблицы:
```
sqlite> .mode csv
sqlite> .import rib.table.lg.ba.ptt.br-BGP.csv rib
```

Проверка схемы созданной таблицы rib:
```
sqlite> .schema rib
CREATE TABLE rib(
  "status" TEXT,
  "network" TEXT,
  "netmask" TEXT,
  "nexthop" TEXT,
  "metric" TEXT,
  "locprf" TEXT,
  "weight" TEXT,
  "path" TEXT,
  "origin" TEXT
);
```

Теперь можно переключить режим на отображение столбцами и посчитать сколько записей в таблице:
```
sqlite> .mode column

sqlite> select count(*) from rib;
count(*)
----------
1068129
```


