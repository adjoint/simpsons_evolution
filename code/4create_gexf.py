# -*- coding: utf-8 -*-

import csv
import copy
import datetime

with open('edges_ID.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
edges = copy.deepcopy(edges0)

with open('characters.csv', 'rb') as f:
    reader = csv.reader(f)
    nodes0 = map(list, reader)
nodes = copy.deepcopy(nodes0)

g = open("simpsons.gexf", "w")

g.write('<?xml version="1.0" encoding="UTF−8"?> \n <gexf> \n')
g.write('<meta>\n')
g.write('<creator>adjoint</creator>\n')
g.write('<description>a dynamic network of the Simpsons universe</description>\n')
g.write('</meta>\n')
g.write('<graph mode="dynamic" defaultedgetype="undirected" timeformat="date" start="1989-12-17" end="2016-12-11">')

counter = 1
g.write('<nodes>\n')
for n in nodes:
    print counter
    counter +=1
    ID = n[0]
    date = n[1]
    name = n[2]
    new_date = datetime.datetime.strptime(date, '%B %d %Y').strftime('%Y-%m-%d')
    g.write('<node id="' + ID + '" label="' + name + '" start="' + new_date + '"/>\n')
g.write('</nodes>\n')

g.write('<edges>\n')
edgeCounter = 1
for e in edges:
    print edgeCounter
    s = e[0]
    t = e[1]
    date = e[2]
    if date != "?":
        new_date = datetime.datetime.strptime(date, '%B %d %Y').strftime('%Y-%m-%d')
        g.write('<edge id="' + str(edgeCounter) + '" source="' + s + '" target="' + t + '" start="' + new_date + '"/>\n')
        edgeCounter += 1

g.write('</edges>\n')
g.write('</graph>\n')
g.write('</gexf>\n')
g

