# LAB 6 : Apache HBase
## 1. HBase CLI
### 1.1 First Commands
#### 1.1.1 Base commands

- Connect to Hadoop Cluster
```console
cdrault> ssh cdrault@hadoop-edge01.efrei.online
```

- Initiate Kerberos ticket
```console
[cdrault@hadoop-edge01 ~] kinit cdrault@EFREI.ONLINE
```

- Type the command `hbase shell`
```console
[cdrault@hadoop-edge01 ~] hbase shell

SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/usr/hdp/3.1.5.0-152/hadoop/lib/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/hdp/3.1.5.0-152/hbase/lib/client-facing-thirdparty/slf4j-log4j12-1.7.25.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.1.6.3.1.5.0-152, rUnknown, Thu Dec 12 20:16:57 UTC 2019
Took 0.0032 seconds
```

- Type some commands
```console
hbase(main):001:0> status
1 active master, 1 backup masters, 3 servers, 0 dead, 61.6667 average load
Took 0.3860 seconds

hbase(main):002:0> version
2.1.6.3.1.5.0-152, rUnknown, Thu Dec 12 20:16:57 UTC 2019
Took 0.0003 seconds

hbase(main):003:0> whoami
cdrault@EFREI.ONLINE (auth:KERBEROS)
    groups: cdrault, hadoop-users
Took 0.0135 seconds

hbase(main):004:0> list
TABLE
ATLAS_ENTITY_AUDIT_EVENTS
aarigonimi:tb_bigdata
acarnez:trees
aelquarati:tree
afischmeister:library
afischmeister:mytable
agoncalves:emp
agoubeau:library
aledeuf:emp
aledeuf:tb_formation
aledeuf:test
amichel:library
aoudni:test
aoudni:trees
apauly:tp_bigdata
apignerol:trees
atlas_titan
bgrandjean:library
bhamdi:library
cazeufack:library
ccarayon:Etudiant
ccarayon:client
ccarayon:emp
ccarayon:library
...

hbase(main):006:0> exit
```
