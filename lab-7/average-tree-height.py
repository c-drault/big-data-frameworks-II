#!/usr/bin/python
from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "AverageTreeHeight"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/share/paris/arbres.csv")
trees = file.map(lambda line: Arbre(line))
heights = trees.map(lambda tree: tree.hauteur())
good_heights = heights.filter(lambda val: is not None)

average = good_heights.sum()/good_heights.count()
print "Average of heights : ",average
