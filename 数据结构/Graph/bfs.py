#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 4:58 PM
# @Author  : Charles He
# @File    : bfs.py
# @Software: PyCharm

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentvert = vertQueue.dequeue()
        for nbr in currentvert.getConnection():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentvert.getDistance() + 1)
                nbr.setPred(currentvert)
                vertQueue.enqueue(nbr)
        currentvert.setColor('black')


def traverse(y):
    x = y
    while x.getPred():
        print(x.getID())
        x = x.getPred
    print(x.getID())