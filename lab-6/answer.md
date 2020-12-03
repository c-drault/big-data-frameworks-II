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

#### 1.1.2 Create own namespace
- Create namespace
```console
hbase(main):001:0> create_namespace 'cdrault'
Took 0.6221 seconds
```

#### 1.1.3 Create table
- Create table in your namespace
```console
hbase(main):004:0> create 'cdrault:library', {NAME => 'author', VERSIONS => 2}, {NAME => 'book', VERSIONS => 3}
Created table cdrault:library
Took 1.3273 seconds
=> Hbase::Table - cdrault:library
```

- Describe the table structure
```console
hbase(main):006:0> desc 'cdrault:library'
Table cdrault:library is ENABLED
cdrault:library
COLUMN FAMILIES DESCRIPTION
{NAME => 'author', VERSIONS => '2', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE => 'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTE
R => 'ROW', CACHE_INDEX_ON_WRITE => 'false', IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536'}
{NAME => 'book', VERSIONS => '3', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE => 'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER
=> 'ROW', CACHE_INDEX_ON_WRITE => 'false', IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536'}
2 row(s)
Took 0.1352 seconds
```

#### 1.1.4
- Add data in table
```console
hbase(main):007:0> put 'cdrault:library', 'vhugo', 'author:lastname', 'Hugo'
Took 0.3839 seconds
hbase(main):008:0> put 'cdrault:library', 'vhugo', 'author:firstname', 'Victor'
Took 0.0056 seconds
hbase(main):009:0> put 'cdrault:library', 'vhugo', 'book:title', 'La légende des siècles'
Took 0.0047 seconds
hbase(main):010:0> put 'cdrault:library', 'vhugo', 'book:category', 'Poèmes'
Took 0.0052 seconds
hbase(main):011:0> put 'cdrault:library', 'vhugo', 'book:year', 1855
Took 0.0042 seconds
hbase(main):012:0> put 'cdrault:library', 'vhugo', 'book:year', 1877
Took 0.0044 seconds
hbase(main):013:0> put 'cdrault:library', 'vhugo', 'book:year', 1883
Took 0.0067 seconds
hbase(main):015:0> put 'cdrault:library', 'jverne', 'author:lastname', 'Verne'
Took 0.0195 seconds
hbase(main):016:0> put 'cdrault:library', 'jverne', 'author:fristname', 'Jules'
Took 0.0051 seconds
hbase(main):017:0> put 'cdrault:library', 'jverne', 'book:publisher', 'Hetzel'
Took 0.0049 seconds
hbase(main):018:0> put 'cdrault:library', 'jverne', 'book:title', 'Face au drapeau'
Took 0.0049 seconds
hbase(main):019:0> put 'cdrault:library', 'jverne', 'book:year', 1896
Took 0.0050 seconds
```

#### 1.1.5 Counting values
- Count values
```console
hbase(main):023:0> count 'cdrault:library'
2 row(s)
Took 0.0135 seconds
=> 2
```

#### 1.1.6 Retrieving values
- get vhugo
```console
get 'cdrault:library', 'vhugo'
COLUMN                                                                CELL
 author:firstname                                                     timestamp=1606988217567, value=Victor
 author:lastname                                                      timestamp=1606988192206, value=Hugo
 book:category                                                        timestamp=1606988295025, value=Po\xC3\xA8mes
 book:title                                                           timestamp=1606988262475, value=La l\xC3\xA9gende des si\xC3\xA8cles
 book:year                                                            timestamp=1606988325116, value=1883
1 row(s)
Took 0.0553 seconds
```

- get vhugo author
```console
hbase(main):025:0> get 'cdrault:library', 'vhugo', 'author'
COLUMN                                                                CELL
 author:firstname                                                     timestamp=1606988217567, value=Victor
 author:lastname                                                      timestamp=1606988192206, value=Hugo
1 row(s)
Took 0.0268 seconds
```

- get vhugo author firstname
```console
hbase(main):026:0> get 'cdrault:library', 'vhugo', 'author:firstname'
COLUMN                                                                CELL
 author:firstname                                                     timestamp=1606988217567, value=Victor
1 row(s)
Took 0.0052 seconds
```

- get jverne book
```console
hbase(main):027:0> get 'cdrault:library', 'jverne', COLUMN=>'book'
COLUMN                                                                CELL
 book:publisher                                                       timestamp=1606988635351, value=Hetzel
 book:title                                                           timestamp=1606988656959, value=Face au drapeau
 book:year                                                            timestamp=1606988674273, value=1896
1 row(s)
Took 0.0091 seconds
```

- Get jverne book title
```console
hbase(main):028:0> get 'cdrault:library', 'jverne', COLUMN=>'book:title'
COLUMN                                                                CELL
 book:title                                                           timestamp=1606988656959, value=Face au drapeau
1 row(s)
Took 0.0049 seconds
```

- Get jverne book title, publisher year
```console
hbase(main):029:0> get 'cdrault:library', 'jverne', COLUMN=>['book:title', 'book:year', 'book:publisher']
COLUMN                                                                CELL
 book:publisher                                                       timestamp=1606988635351, value=Hetzel
 book:title                                                           timestamp=1606988656959, value=Face au drapeau
 book:year                                                            timestamp=1606988674273, value=1896
1 row(s)
Took 0.0235 seconds
```

- Values
```console
hbase(main):030:0> get 'cdrault:library', 'jverne', FILTER=>"ValueFilter(=, 'binary:Jules')"
COLUMN                                                                CELL
 author:fristname                                                     timestamp=1606988605951, value=Jules
1 row(s)
Took 0.0372 seconds
```

#### 1.1.7 Tuble browsing
- Displays all the data
```console
hbase(main):032:0> scan 'cdrault:library'
ROW                                                                   COLUMN+CELL
 jverne                                                               column=author:fristname, timestamp=1606988605951, value=Jules
 jverne                                                               column=author:lastname, timestamp=1606988594404, value=Verne
 jverne                                                               column=book:publisher, timestamp=1606988635351, value=Hetzel
 jverne                                                               column=book:title, timestamp=1606988656959, value=Face au drapeau
 jverne                                                               column=book:year, timestamp=1606988674273, value=1896
 vhugo                                                                column=author:firstname, timestamp=1606988217567, value=Victor
 vhugo                                                                column=author:lastname, timestamp=1606988192206, value=Hugo
 vhugo                                                                column=book:category, timestamp=1606988295025, value=Po\xC3\xA8mes
 vhugo                                                                column=book:title, timestamp=1606988262475, value=La l\xC3\xA9gende des si\xC3\xA8cles
 vhugo                                                                column=book:year, timestamp=1606988325116, value=1883
2 row(s)
Took 0.0136 seconds
```

- Displays only data from book family
```console
hbase(main):034:0> scan 'cdrault:library', { COLUMN=> 'book'}
ROW                                                                   COLUMN+CELL
 jverne                                                               column=book:publisher, timestamp=1606988635351, value=Hetzel
 jverne                                                               column=book:title, timestamp=1606988656959, value=Face au drapeau
 jverne                                                               column=book:year, timestamp=1606988674273, value=1896
 vhugo                                                                column=book:category, timestamp=1606988295025, value=Po\xC3\xA8mes
 vhugo                                                                column=book:title, timestamp=1606988262475, value=La l\xC3\xA9gende des si\xC3\xA8cles
 vhugo                                                                column=book:year, timestamp=1606988325116, value=1883
2 row(s)
Took 0.0276 seconds
```

- Displays only year of book
```console
hbase(main):035:0> scan 'cdrault:library', { COLUMN=> 'book:year'}
ROW                                                                   COLUMN+CELL
 jverne                                                               column=book:year, timestamp=1606988674273, value=1896
 vhugo                                                                column=book:year, timestamp=1606988325116, value=1883
2 row(s)
Took 0.0064 seconds
```

- The first scan scans the tuples by keys between a and n and the fields of the family author.
```console

```

- The second does exactly the same, but with a lter.
```console

```

- The third scan displays the author values: rstname.
```console

```

- The fourth scan searches for columns whose value equals the specified title.
```console

```

- The fifth displays the tuples whose (latest version of the) book column: date is less than or equal to 1890.
```console

```

- The last filter is more complex, it searches for tuples whose key begins with jv and one of the values of which matches the regular expression: [A-Z]([a-z]+ )2,.
```console

```

#### 1.1.8 Updating a value
```console
hbase(main):037:0> put 'cdrault:library', 'vhugo', 'author:lastname', 'HAGO'
Took 0.0811 seconds

hbase(main):038:0> put 'cdrault:library', 'vhugo', 'author:lastname', 'HUGO'
Took 0.0045 seconds

hbase(main):039:0> put 'cdrault:library', 'vhugo', 'author:firstname', 'Victor Marie'
Took 0.0048 seconds

hbase(main):040:0> put 'cdrault:library', 'vhugo', 'author:lastname', 'Hugo'
Took 0.0058 seconds

hbase(main):041:0> get 'cdrault:library', 'vhugo', 'author'
COLUMN                                                                CELL
 author:firstname                                                     timestamp=1607004728591, value=Victor Marie
 author:lastname                                                      timestamp=1607004746206, value=Hugo
1 row(s)
Took 0.0130 seconds

hbase(main):042:0> get 'cdrault:library', 'vhugo', COLUMNS=>'author'
COLUMN                                                                CELL
 author:firstname                                                     timestamp=1607004728591, value=Victor Marie
 author:lastname                                                      timestamp=1607004746206, value=Hugo
1 row(s)
Took 0.0136 seconds

hbase(main):043:0> get 'cdrault:library', 'vhugo', COLUMNS=>'author', VERSIONS=>10
COLUMN                                                                CELL
 author:firstname                                                     timestamp=1607004728591, value=Victor Marie
 author:firstname                                                     timestamp=1606988217567, value=Victor
 author:lastname                                                      timestamp=1607004746206, value=Hugo
 author:lastname                                                      timestamp=1607004700169, value=HUGO
1 row(s)
Took 0.0074 seconds
```

#### 1.1.9 Deleting a value or a column
- The first deleteall deleted the value author:name=HUGO, but not the other (unless you have entered the wrong timestamp).
```console
hbase(main):044:0> deleteall 'cdrault:library', 'vhugo', 'author:lastname', 1607004700169
Took 0.0197 seconds
```

- The second deleted then all values for the column firstname.
```console
hbase(main):052:0> deleteall 'cdrault:library', 'vhugo', 'author:firstname'
Took 0.0202 seconds
```

- The last deleteall deleted the entire tuple.
```console
hbase(main):002:0> deleteall 'cdrault:library', 'vhugo'
Took 0.3790 seconds
hbase(main):003:0> deleteall 'cdrault:library', 'jverne'
Took 0.0064 seconds
```

- Use scan command to check the version 10.
```console
hbase(main):004:0> scan 'cdrault:library'
ROW                                                                   COLUMN+CELL
0 row(s)
Took 0.0089 seconds
```

#### 1.1.10 Deleting table
- Disable the table
```console
hbase(main):005:0> disable 'cdrault:library'
Took 0.9824 seconds
```

- Drop the table
```console
hbase(main):006:0> drop 'cdrault:library'
Took 0.4635 seconds
```

