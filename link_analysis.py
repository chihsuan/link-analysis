#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import re
import numpy as np
import operator

from my_class.Graph import Graph
from modules.hits import hits
from modules.page_rank import page_rank
from modules.sim_rank import sim_rank
from modules import json_io

def read_graph(f):
    graph = {}
    nodes = []
    for line in f.readlines():
        source, target = parse_format(line)
        if source not in graph:
            graph[source] = [target]
        else:
            graph[source].append(target)

        if source not in nodes:
            nodes.append(source)
        if target not in nodes:
            nodes.append(target)

    return Graph(graph, nodes)

def parse_format(line):
    source, target = line.split(',')
    match = re.search('([0-9]+)', target)
    if match:
        target = match.groups()[0]
    return source, target


if __name__=='__main__':
    
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: <file>"
        exit(-1)
   
    if sys.argv[1][-4:] != 'json':
        f = open(sys.argv[1])
        graph = read_graph(f)
    else:
        graph = json_io.read_json(sys.argv[1])
        movie_dic = json_io.read_json(sys.argv[2])
        nodes = movie_dic.keys()
        for i in xrange(len(nodes)):
            nodes[i] = str(nodes[i])
        graph = Graph(graph, nodes)


    rank = page_rank(graph, 20, 0.85)

    auth, hubs = hits(graph, 40)
    sorted_auth = sorted(auth.items(), key=operator.itemgetter(1))
    sorted_hubs = sorted(hubs.items(), key=operator.itemgetter(1))


    if sys.argv[1][-4:] != 'json':
        sim = sim_rank(graph)
        json_io.write_json(output_path + '_sim.json', sim)
        f.close()


    output_path = 'dist/' + sys.argv[1].split('/')[1][:-4] 
    json_io.write_json(output_path + '_rank.json', rank)
    json_io.write_json(output_path + '_auth.json', auth)
    json_io.write_json(output_path + '_hubs.json', hubs)
