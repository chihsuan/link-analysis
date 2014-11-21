#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import math

def hits(graph, iteration=5, min_delta=0.0001):
    auth = dict.fromkeys(graph.nodes, 1.0)
    hubs = dict.fromkeys(graph.nodes, 1.0)

    for iteration in xrange(int(iteration)):
        for node in graph.nodes:
            auth[node] = sum_hubs(graph, node, hubs)
        auth = normalization(auth)

        old_hub = hubs.copy()
        for node in graph.nodes:       
            hubs[node] = sum_authorities(graph, node, auth)
        hubs = normalization(hubs)

        delta = sum((abs(old_hub[k] - hubs[k]) for k in hubs))
        if delta <= min_delta:
            return (auth, hubs)

    return (auth, hubs)

def sum_hubs(graph, node, hubs):
    s_hubs = 0.0
    if node not in graph.in_nodes:
        return s_hubs

    for in_node in graph.in_nodes[node]:
        s_hubs += hubs[in_node]
    return s_hubs

def sum_authorities(graph, node, authorities):
    s_authorities = 0.0

    if node not in graph.out_nodes:
        return s_authorities

    for in_node in graph.out_nodes[node]:
        s_authorities += authorities[in_node]
    return s_authorities

def normalization(dic):
    norm = sum((dic[p] for p in dic))
    return {k: v / norm for (k, v) in dic.items()}

