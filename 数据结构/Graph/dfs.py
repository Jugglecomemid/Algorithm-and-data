#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 4:58 PM
# @Author  : Charles He
# @File    : dfs.py
# @Software: PyCharm

from pythonds.graphs import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0


    def dfs(self):
        for vertx in self:
            vertx.setColor('white')
            vertx.setPred(-1)
        for vertx in self:
            if vertx.getColor() == 'white':
                self.dfsvisit(vertx)

    def dfsvisit(self, startVertx):
        startVertx.setColor('gray')
        self.time += 1
        startVertx.setDiscovery(self.time)

        # 如果到底层 就跳过递归
        for nextVertx in startVertx.getConnections():
            if nextVertx.getColor() == 'white':
                nextVertx.setPred(startVertx)
                self.dfsvisit(nextVertx)
        startVertx.setColor('black')
        self.time += 1
        startVertx.setFinish(self.time)

