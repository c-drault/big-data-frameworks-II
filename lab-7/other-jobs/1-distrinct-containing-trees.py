#!/usr/bin/python
from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "distrinctContainingtrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")
trees = file.map(lambda line: Tree(line))

districts = trees.map(lambda tree: tree.district())
coll = districts.collect()
print "Districts : %s" % (coll)
