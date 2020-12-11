#!/usr/bin/python

from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "sortBySmallerTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")
trees = file.map(lambda line: Tree(line))

species = trees.map(lambda tree: (tree.height(), tree.specie()) )
species_f = species.filter(lambda (h, s) : h is not None and s is not None)
species_sort = species_f.sortByKey()
print "Height, Specie : %s" % (species_sort.collect())
