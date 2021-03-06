#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys

class Graph:

    def __init__(self, graph, nodes):
        self.graph = graph
        self.nodes = nodes
        self.in_nodes = self.get_in_nodes()
        self.out_nodes = graph

    def get_in_nodes(self):
        in_nodes = {}
        for node in self.nodes:
            in_nodes[node] = []
        
        for source, targets in self.graph.iteritems():
            for node in targets:
                if str(source) not in in_nodes[str(node)]:
                    in_nodes[str(node)].append(str(source))
        return in_nodes
         


