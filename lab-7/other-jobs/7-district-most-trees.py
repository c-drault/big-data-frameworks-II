#!/usr/bin/python
from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "dsitrictMoreTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")

trees = file.map(lambda line: Tree(line))
district = trees.map(lambda tree: tree.district())
district_f = district.filter(lambda d: d is not None)
district_map = district_f.map(lambda d: (d, 1) )
district_reduce = district_map.reduceByKey(lambda a,b: a+b)
district_max = district_reduce.max(lambda d:d[1] )

print "District, number of trees : ", district_max
