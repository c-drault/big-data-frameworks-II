#!/usr/bin/python

from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "sortBySmallerTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")
trees = file.map(lambda line: Tree(line))

district = trees.map(lambda tree: (tree.year(), tree.district()) )
district_f = district.filter(lambda (y, d) : y is not None and d is not None)

district_min = district_f.min()
print "Year , District : ", district_min
