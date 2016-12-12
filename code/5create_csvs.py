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

f = open("nodes.csv", "w")
g = open("edges.csv", "w")
f.write("ID,label,start\n")
g.write("source,target,start,type\n")

counter = 1
for n in nodes:
    print counter
    counter+=1
    ID = n[0]
    date = n[1]
    if date == "September 252016":
        date = "September 25 2016"
    name = n[2]
    new_date = datetime.datetime.strptime(date, '%B %d %Y').strftime('%Y-%m-%d')
    f.write(ID + ',' + name + ',' + new_date + '\n')

edgeCounter = 1
for e in edges:
    print edgeCounter
    edgeCounter += 1
    s = e[0]
    t = e[1]
    date = e[2]
    if date == "September 252016":
        date = "September 25 2016"
    if date != "?":
        new_date = datetime.datetime.strptime(date, '%B %d %Y').strftime('%Y-%m-%d')
        g.write(s + ',' + t + ',' + new_date + ',undirected\n')
        

f.close()
g.close()


