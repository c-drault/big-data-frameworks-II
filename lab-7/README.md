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
- Displays the list of distinct containing trees, [python script](other-jobs/1-distrinct-containing-trees.py);
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py other-jobs/1-distrinct-containing-trees.py
```

- Displays the list of different species trees, [python script](other-jobs/2-different-species-trees.py);
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py other-jobs/2-different-species-trees.py
```

- The number of trees of each kind, [python script](other-jobs/3-number-of-trees-each-kind.py);
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py other-jobs/3-number-of-trees-each-kind.py
```

- Calculates the height of the tallest tree of each kind, [python script](other-jobs/4-tallest-tree-each-kind.py);
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py other-jobs/4-tallest-tree-each-kind.py
```

- Sort the trees height from smallest to largest, [python script](other-jobs/5-sort-smaller-tree.py);
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py other-jobs/5-sort-smaller-tree.py
```

- Displays the district where the oldest tree is, [python script](other-job/6-oldest-tree-district.py);
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py other-jobs/6-oldest-tree-district.py
```

- Displays the district that contains the most trees, [python script](other-job/7-district-most-trees.py);
```console
[cdrault@hadoop-edge01 ~] spark-submit --master=yarn --py-files tree.py other-jobs/7-district-most-trees.py
```
