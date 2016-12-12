# -*- coding: utf-8 -*-

import csv
import copy
import datetime

with open('edges.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
edges = copy.deepcopy(edges0)


g = open("filtered_edges.csv", "w")
g.write("source,target,start,type\n")

e_list = {}

edgeCounter = 1
for e in edges:
    print edgeCounter
    edgeCounter += 1
    s = e[0]
    t = e[1]
    start = e[2]
    typ = e[3]
    if (s, t) not in e_list and s!="" and t!="":
        e_list[(s,t)] = 1
        g.write(s + "," + t + "," + start + "," + typ + "\n")
        

g.close()


