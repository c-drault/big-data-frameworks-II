# LAB 3
## 1.1 Create a Connection to Beeline Client
- Connect to Hadoop Cluster using SSH 
```console
cdrault> ssh tp2user@hadoop-edge01.efrei.online
```

- Initialize a Kerberos Ticket
```console
[cdrault@hadoop-edge01 ~] kinit cdrault@EFREI.ONLINE
```

- Type the command beeline in the terminal prompt, when prompted press enter as username and as password.
```console
[cdrault@hadoop-edge01 ~] beeline
```

- Connect to the Hive using the command `!connect`
```console
0: jdbc:hive2://hadoop-master01.efrei.online:> !connect jdbc:hive2://hadoop-master01.efrei.online:2181,hadoop-master02.efrei.online:2181,hadoop-master03.efrei.online:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2 cdrault PASSWORD
```

- Type help command for list of beeline commands.
```
Juste type help.
```

- Which command allows you to view the jdbc connection used to connect to HiveServer2?
```console
!typeinfo
```

- List all databases.
```console
SHOW DATABASES;
```

- If not exists, create a database using your username.
```console
CREATE DATABASE cdrault;
```

- Use your database.
```console
USE cdrault;
```

- List the tables.
```console
!sql SHOW TABLES;
```

- Create table called temp with a column called col of String type.
```console
!sql CREATE TABLE temp (col string);
```

- Confirm the table creation.
```console
!sql SHOW TABLES;
+-----------+
| tab_name  |
+-----------+
| temp      |
+-----------+
```

- List the columns (name, data type, etc) of temp table.
```console
!sql desc temp;
+-----------+------------+----------+
| col_name  | data_type  | comment  |
+-----------+------------+----------+
| col       | string     |          |
+-----------+------------+----------+
```

- Remove the table.
```console
!sql drop table temp;
!sql SHOW TABLES;
+-----------+
| tab_name  |
+-----------+
+-----------+
```

- Type !quit to exit the beeline shell.
```console
!quit
```

## 1.2 Create tables
You are going to write some Hive SQL queries on the remarkable trees of Paris
using this dataset.
- Create an external table called `trees_external`.
```console
CREATE EXTERNAL TABLE IF NOT EXISTS trees_external (
  GEOPOINT String,
  ARRONDISSEMENT String, 
  GENRE String,
  ESPECE String,
  FAMILLE String,
  ANNEE_PLANTATION String,
  HAUTEUR String,
  CIRCONFERENCE String,
  ADRESSE String,
  NOM_COMMUN String,
  VARIETE String,
  OBJECTID String,
  NOM_EV String
);
```

- Create an internal table called `trees_internal`.
```console
CREATE TABLE IF NOT EXISTS trees_internal (
  GEOPOINT String,
  ARRONDISSEMENT String, 
  GENRE String,
  ESPECE String,
  FAMILLE String,
  ANNEE_PLANTATION String,
  HAUTEUR String,
  CIRCONFERENCE String,
  ADRESSE String,
  NOM_COMMUN String,
  VARIETE String,
  OBJECTID String,
  NOM_EV String
);
```
- Import data to the internal table using the external table.


- Verify that each table got the same lines count.

## 1.3 Create queries
In this part, you are going to do the same queries as MapReduce ones using the
internal table created before. You will create queries that:
- displays the list of distinct containing trees;
- displays the list of different species trees;
- the number of trees of each kind;
- calculates the height of the tallest tree of each kind;
- sort the trees height from smallest to largest;
- displays the district where the oldest tree is;
- displays the district that contains the most trees;
