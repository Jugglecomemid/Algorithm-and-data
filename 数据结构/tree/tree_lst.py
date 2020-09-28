#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 2:38 PM
# @Author  : Charles He
# @File    : tree_lst.py
# @Software: PyCharm


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == "__main__":
    r = BinaryTree(3)
    insertLeft(r, 4)
    print(r)
    insertLeft(r, 5)
    print(r)
