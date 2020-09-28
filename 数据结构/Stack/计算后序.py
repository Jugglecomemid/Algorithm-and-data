#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 10:38 AM
# @Author  : Charles He
# @File    : 计算后序.py
# @Software: PyCharm

from pythonds.basic import Stack


def cal_postfix(postfixExpr):
    opStack = Stack()

    token_lst = postfixExpr.split()

    for token in token_lst:
        if token in "0123456789":
            opStack.push(int(token))

        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            result = do_math(token, op1, op2)
            opStack.push(result)

    return opStack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2

    elif op == "/":
        return op1 / op2

    elif op == "+":
        return op1 + op2

    elif op == "-":
        return op1 - op2


if __name__ == "__main__":
    result = cal_postfix("1 2 3 * +")  # 7
    print(result)
