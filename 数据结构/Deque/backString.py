#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 10:27 AM
# @Author  : Charles He
# @File    : backString.py
# @Software: PyCharm

from Deque import Deque


def backString_detect(aString):
    charDeque = Deque()

    for ch in aString:
        charDeque.addRear(ch)

    stillEqual = True

    while charDeque.size()>1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == "__main__":
    print(backString_detect('radar'))
