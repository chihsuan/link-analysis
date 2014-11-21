#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import numpy as np
import itertools 

def sim_rank(graph, C=0.9, iteration=20, min_delta=0.85):
    sim = np.identity(len(graph.nodes))
    old_sim = np.zeros(len(graph.nodes))
    for itr in xrange(int(iteration)):
        old_sim = np.copy(sim)
        for a, b in itertools.product(graph.nodes, graph.nodes):
            if a is b or len(graph.in_nodes[a]) == 0 or len(graph.in_nodes[b]) == 0:
                continue
            s_ab = 0
            for na in graph.in_nodes[a]:
                for nb in graph.in_nodes[b]:
                    s_ab += old_sim[int(na)-1][int(nb)-1]
             
            sim[int(a)-1][int(b)-1] =  s_ab * C / len(graph.in_nodes[a]) * len(graph.in_nodes[b])

    return sim

