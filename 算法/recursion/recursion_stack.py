#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 10:33 AM
# @Author  : Charles He
# @File    : recursion_stack.py
# @Software: PyCharm


from pythonds import Stack

rStack = Stack()


def toStr(n, base):
    convertStr = '0123456789ABCDEF'

    if n < base:
        rStack.push(convertStr[n])
    else:
        rStack.push(convertStr[n % base])
        toStr(n // base, base)
