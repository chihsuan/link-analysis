#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import urllib2

from bs4 import BeautifulSoup
from modules import json_io

def movie_graph(urls):
    pages = {}
    pages_dic = {}
    graph = {}    
    count = 1
    curr_count = 1

    for url in urls:
        page = http_get(url) 
        soup, movie_title = get_movie_title(page)
        rec_items = soup.find_all('div', class_='rec_item')
        
        if movie_title not in pages_dic:
            curr_count = count
            count += 1
        else:
            curr_count = pages_dic[movie_title]
        graph[curr_count] = []

        print '---' + movie_title + '---'
        
        for item in rec_items:
            link = 'http://www.imdb.com/' + item.find('a').get('href')
            out_page = http_get(link)
            _soup, title = get_movie_title(out_page)
            print title,
            if title not in pages_dic:
                pages[count] = title
                pages_dic[title] = count
                graph[curr_count].append(count)
                count += 1
            else:
                graph[curr_count].append(pages_dic[title])

        print
        pages[curr_count] = movie_title
        pages_dic[movie_title] = curr_count

    return pages, graph

def get_movie_title(page):
    soup = BeautifulSoup(page)
    
    movie_title = soup.find('h1', class_='header') \
                      .find('span', class_='itemprop') \
                      .get_text()

    return soup, movie_title

def http_get(url):
    return urllib2.urlopen(url).read()

if __name__=='__main__':
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: <file>"
        exit(-1)

    f = open(sys.argv[1])

    urls = f.readlines()

    pages, graph = movie_graph(urls)
    f.close()

    json_io.write_json('dataset/imdb.json', pages)
    json_io.write_json('dataset/graph_9.json', graph)
