# -*- coding: utf-8 -*-

import csv
import copy
import datetime

with open('edges.csv', 'rb') as f:
    reader = csv.reader(f)
    edges0 = map(list, reader)
    del edges0[0]
edges = copy.deepcopy(edges0)


g = open("weighted_edges.csv", "w")
g.write("source,target,start,end,weight,type\n")
errors = open("errors.csv", "w")

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
        e_list[(s,t)] = [start]
    else:
        e_list[(s,t)].append(start)

default_end = "2016-12-11"

for tup in e_list:
    s = tup[0]
    t = tup[1]
    dates = e_list[(s,t)]
    weight = 1
    for i in range(len(dates) - 1):
        start = dates[i]
        end = dates[i+1]
        g.write(s + "," + t + "," + start + "," + end + "," + str(weight) + ",undirected\n")
        weight+=1
    g.write(s + "," + t + "," + dates[-1] + "," + default_end + "," + str(weight) + ",undirected\n")

g.close()


