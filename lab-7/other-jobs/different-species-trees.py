#!/usr/bin/python

from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "distinctContainingTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")

trees = file.map(lambda line: Tree(line))
species = trees.map(lambda tree: tree.specie())
species_f = trees.filter(lambda s: s is not None)
species_d = species_f.distinct()
print "Species : %s" % (species_d.collect())