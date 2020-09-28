#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 10:07 AM
# @Author  : Charles He
# @File    : 中序到后序转换.py
# @Software: PyCharm

from pythonds.basic import Stack
import string


def infix2postfix(infix):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opStack = Stack()
    postfixLst = []

    token_lst = infix.split()

    for token in token_lst:
        if token in string.ascii_uppercase:
            postfixLst.append(token)

        elif token == '(':
            opStack.push(token)

        elif token == ')':
            topToken = opStack.pop()
            while topToken != "(":
                postfixLst.append(topToken)
                topToken = opStack.pop()

        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):  # peek可看顶端元素
                postfixLst.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixLst.append(opStack.pop())

    return " ".join(postfixLst)


if __name__ == "__main__":
    result1 = infix2postfix("A + B * C")
    result2 = infix2postfix("( A + B ) * C")
    result3 = infix2postfix("( A + B ) * ( C + D )")
    print(result1)
    print("-----------------")
    print(result2)
    print("-----------------")
    print(result3)
