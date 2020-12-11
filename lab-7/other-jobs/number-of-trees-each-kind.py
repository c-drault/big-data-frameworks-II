
#!/usr/bin/python

from pyspark import SparkConf, SparkContext
from tree import Tree

appName = "distinctContainingTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

file = sc.textFile("hdfs:/user/cdrault/trees.csv")

trees = file.map(lambda line: Tree(line))
species = trees.map(lambda tree: tree.specie())
species_f = species.filter(lambda s: s is not None)

species_map = species_f.map(lambda species : (species, 1))
species_reduce = species_map.reduceByKey(lambda a,b: a+b)
print "Species and number : %s" % (species_reduce.collect())
