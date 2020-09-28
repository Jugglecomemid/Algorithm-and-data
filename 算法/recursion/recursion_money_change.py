#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 2:52 PM
# @Author  : Charles He
# @File    : recursion_money_change.py
# @Software: PyCharm


""" This part also contains dynamic programming"""


def charge(coinValueLst, money):
    """
    This part takes huge calculation and should be modified.
    :param coinValueLst:
    :param money:
    :return:
    """
    mincoins = money
    if mincoins in coinValueLst:
        return 1

    else:
        for i in [c for c in coinValueLst if c <= money]:
            num_coins = 1 + charge(coinValueLst, money - i)
            if num_coins < mincoins:  # 一直递归找最少的
                mincoins = num_coins

    return mincoins


def charge_better(coinValueLst, money, knownResults):
    """
    Better than the above one but not enough.
    :param coinValueLst:
    :param money:
    :param knownResults:
    :return:
    """
    mincoins = money
    if money in coinValueLst:
        knownResults[money] = 1
        return 1

    elif knownResults[money] > 0:
        return knownResults[money]

    else:
        for i in [c for c in coinValueLst if c <= money]:
            num_coins = 1 + charge_better(coinValueLst, money - i, knownResults)
            if num_coins < mincoins:
                mincoins = num_coins
                knownResults[money] = mincoins
    return mincoins


def dp_charge(coinValueLst, money, mincoins):
    for cent in range(money+1):
        coinCount = cent
        for i in [c for c in coinValueLst if c <= cent]:
            if mincoins[cent - i] + 1 < coinCount:  # 关键是这一句
                coinCount = mincoins[cent - i] + 1
        mincoins[cent] = coinCount

    return mincoins[money]


if __name__ == "__main__":
    result = charge_better([1, 5, 10, 25], 26, [0]*27)
    print(result)
