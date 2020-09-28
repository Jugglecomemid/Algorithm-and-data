#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 10:21 AM
# @Author  : Charles He
# @File    : Deque.py
# @Software: PyCharm


class Deque:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def addFront(self, item):
        self.item.append(item)

    def addRear(self, item):
        self.item.insert(0, item)

    def removeFront(self):
        self.item.pop()

    def removeRear(self):
        self.item.pop(0)

    def size(self):
        return len(self.item)
