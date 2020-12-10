#!/usr/bin/env python
from pyspark import SparkConf, SparkContext

appName = "numberOfTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

#open file
file = sc.textFile("hdfs:///user/cdrault/trees.csv")

#Number of line
number = file.count()
print "Number of lines :", number
