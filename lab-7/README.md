# LAB 7 : Apache Spark
## 1. Introduction

- Connect to Hadoop Cluster and Kerberos
```console
cdrault> ssh cdrault@hadoop-edge01.efrei.online
[cdrault@hadoop-edge01 ~] kinit cdrault@EFREI.ONLINE
```

## 2.Tutorial
### 2.2 Number of trees
- Execute [number-of-trees.py](number-of-trees.py)
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn number-of-trees.py
```

### 2.3 Average Tree Height
- Execute [average-tree-height.py](average-tree-height.py) with the [tree.py](tree.py)
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py average-tree-height.py
```

### 2.4
- Displays the list of distinct containing trees;
```console
[cdrault@hadoop-edge01 ~]
```

- Displays the list of different species trees;
```console
[cdrault@hadoop-edge01 ~]
```

- The number of trees of each kind;
```console
[cdrault@hadoop-edge01 ~]
```

- Calculates the height of the tallest tree of each kind;
```console
[cdrault@hadoop-edge01 ~]
```

- Sort the trees height from smallest to largest;
```console
[cdrault@hadoop-edge01 ~]
```

- Displays the district where the oldest tree is;
```console
[cdrault@hadoop-edge01 ~]
```

- Displays the district that contains the most trees;
```console
[cdrault@hadoop-edge01 ~]
```
