#!/usr/bin/python

class Tree(object):
    def __init__(self, line):
        self.data = line.split(";")

    def __str__(self):
        return "Tree[%s]" % ', '.join(self.data)

    def specie(self):
        if self.data[2] == u'GENRE': return None
        return self.data[2]

    def height(self):
        if self.data[6] == u'HAUTEUR': return None
        try:
            return float(self.data[6])
        except:
            return None
    
    def year(self):
        if self.data[5] == u'ANNEE PLANTATION': return None
        try:
            return int(self.data[5])
        except:
            return None
        
    def district(self):
        if self.data[1] == u'ARRONDISSEMENT': return None
        try:
            return int(self.data[1])
        except:
            return None
