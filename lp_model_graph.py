#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import random

from modules import json_io

def get_lp_graph(grid_size):
    graph = {}
    node = 1
    grid_size += 1

    for i in range(grid_size):
        for j in range(grid_size):
            graph[node] = []
            if i > 0:
                graph[node].append(node - i * grid_size)
            if i < (grid_size-1):
                graph[node].append(node + i * grid_size)
            if j > 0:
                graph[node].append(node - 1)
            if j < (grid_size-1):
                graph[node].append(node + 1)
            node += 1
    return graph

def rewire_edge(graph, prob):
    
    for node, out_nodes in graph.iteritems():
        if random.uniform(0, 1) < prob:
            pick = random.randint(0, len(out_nodes)-1)
                
            new_edge = random.randint(1, len(graph.keys()))
            while new_edge in out_nodes or new_edge == node:
                new_edge = random.randint(1, len(graph.keys()))

            out_nodes.append(new_edge)
            out_nodes.pop(pick)
    return graph

if __name__=='__main__':
    
    p1 = 0.2
    p2 = 0.8

    lp_graph = get_lp_graph(4)
    rewire_graph1 = rewire_edge(lp_graph.copy(), p1)
    rewire_graph2 = rewire_edge(lp_graph.copy(), p2)
    json_io.write_json('dataset/graph7.json', rewire_graph1)
    json_io.write_json('dataset/graph8.json', rewire_graph2)


