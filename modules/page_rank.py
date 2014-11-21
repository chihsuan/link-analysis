#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
from my_class.Graph import Graph

def page_rank(graph, iteration=20, damping_factor=0.85):
    num_nodes = len(graph.nodes)
    ranks = dict.fromkeys(graph.nodes, 1.0/num_nodes)
    
    min_value = 1 - damping_factor
    for itr in xrange(int(iteration)):
        for node in graph.nodes:
            rank = min_value
            for in_node in graph.in_nodes[node]:
                rank = damping_factor * ranks[in_node] / len(graph.out_nodes[in_node])
            ranks[node] = rank
    return ranks

