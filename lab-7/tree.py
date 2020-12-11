#!/usr/bin/python

class Tree(object):
    def __init__(self, line):
        self.data = line.split(";")

    def __str__(self):
        return "Tree[%s]" % ', '.join(self.data)

    def genre(self):
        if self.data[2] == u'GENRE': return None
        return self.data[2]

    def hauteur(self):
        try:
            return float(self.data[6])
        except:
            return None
