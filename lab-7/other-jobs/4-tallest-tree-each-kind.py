#!/usr/bin/python

from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "tallestTreeEachKind"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")

trees = file.map(lambda line: Tree(line))
species = trees.map(lambda tree: (tree.specie(), tree.height()) )
species_f = species.filter(lambda s,h: s is not None and h is not None)

species_reduce = species_f.reduceByKey(lambda a,b: a if a > b else b)
print "Species : %s" % (species_reduce.collect())
