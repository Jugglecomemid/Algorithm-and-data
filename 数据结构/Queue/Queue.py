#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 10:56 AM
# @Author  : Charles He
# @File    : Queue.py
# @Software: PyCharm

class Queue(object):
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def enqueue(self, element):
        return self.item.insert(0, element)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)