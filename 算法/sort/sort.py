#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 9:53 AM
# @Author  : Charles He
# @File    : sort.py
# @Software: PyCharm


def bubbleSort(alist):
    # this one means starting from ending， -1 means bp 1 steps
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
    print(alist)


def selectionSort(alist):
    # start from ending
    for shot in range(len(alist) - 1, 0, -1):
        position = 0
        # suppose len(alist) =10, then 10-->9-->8-->...-->1
        for locaiton in range(1, shot + 1):
            # first round, find the largest and compare to the first one alist[0]
            if alist[locaiton] > alist[position]:
                position = locaiton
        # then put it into the last(10th) position.
        temp = alist[shot]
        alist[shot] = alist[position]  # this one record the largest
        alist[position] = temp
    print(alist)


def insertSort(alist):
    for index in range(1, len(alist)):
        current = alist[index]
        pos = index
        # this part means the smaller current_value is moved forward until stop `   `
        while pos > 0 and alist[pos-1] > current:
            alist[pos] = alist[pos-1]  # largest one stay behind
            pos = pos - 1

        alist[pos] = current
    print(alist)




if __name__ == "__main__":
    insertSort([33, 56, 21, 22])
