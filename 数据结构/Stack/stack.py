#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 9:47 AM
# @Author  : Charles He
# @File    : stack.py
# @Software: PyCharm


class Stack(object):
    def __init__(self):
        self.stack = []

    def is_Empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def pop(self):
        item = self.stack.pop()
        return item

    def append(self, element):
        self.stack.append(element)


