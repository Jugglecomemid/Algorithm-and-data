#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 10:11 AM
# @Author  : Charles He
# @File    : binarySearch.py
# @Software: PyCharm


def binarySearch(orderlist, item):
    first = 0
    last = len(orderlist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if orderlist[midpoint] == item:
            found = True
        else:
            if item < orderlist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binarySearch_rec(orderlist, item):
    """递归版"""
    if len(orderlist) == 0:
        return False
    else:
        midpoint = len(orderlist) // 2
        if orderlist[midpoint] == item:
            return True
        else:
            if item < orderlist[midpoint]:
                return binarySearch_rec(orderlist[:midpoint], item)

            else:
                return binarySearch_rec(orderlist[midpoint + 1:], item)

