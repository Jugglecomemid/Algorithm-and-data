#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 4:17 PM
# @Author  : Charles He
# @File    : math_expression_tree.py
# @Software: PyCharm

import operator
from pythonds.basic import Stack
from pythonds.trees import BinaryTree


def buildParseTree(math_exp):
    lst = math_exp.split()
    pstack = Stack()
    etree = BinaryTree("")
    pstack.push(etree)
    currentTree = etree

    for i in lst:
        if i == "(":
            currentTree = currentTree.insertLeft("")  # 此时尚在根结点（父节点）
            pstack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in "+-*/)":
            currentTree.setRootVal(eval(i))
            parent = pstack.pop()
            currentTree = parent
        elif i in "+-*/":
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pstack.push(currentTree)
        elif i == ")":
            currentTree = pstack.pop()
        else:
            raise ValueError("Unknow Operator:{}".format(i))

    return currentTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, "/": operator.truediv}

    leftNode = parseTree.getLeftChild()
    rightNode = parseTree.getRightChild()

    if leftNode and rightNode:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftNode), evaluate(rightNode))
    else:
        return parseTree.getRootVal()


if __name__ == '__main__':
    math_exp = "(7+1)*(5-3)"
    result = evaluate(buildParseTree(math_exp))
    print(result)
