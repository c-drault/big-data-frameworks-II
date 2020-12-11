#!/usr/bin/python

from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "distinctContainingTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")

trees = file.map(lambda line: Tree(line))

districts = trees.map(lambda tree: tree.district())
districts_filtered = districts.filter(lambda height: height is not None)
districts_distinct = districts_filtered.distinct()
coll = districts_distinct.collect()
print "District containing trees : %s" % (coll)
