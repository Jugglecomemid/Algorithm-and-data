#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 10:56 AM
# @Author  : Charles He
# @File    : quickSort.py
# @Software: PyCharm


def quickSort(lst, i, j):
    # 出口
    if i >= j:
        return lst

    pivot = lst[i]
    low = i
    high = j

    while i < j:
        # 先从后面j开始向前找比pivot小的, 找到就停，然后交换
        while i < j and lst[j] >= pivot:
            j -= 1
        lst[i] = lst[j]
        # 先从前面i开始向后找比pivot大的, 找到就停，然后交换
        while i < j and lst[i] <= pivot:
            i += 1
        lst[j] = lst[i]

    # 当i>=j 时 pivot移动到j
    lst[j] = pivot

    quickSort(lst, low, i - 1)
    quickSort(lst, i + 1, high)
    return lst


if __name__ == "__main__":
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print("排序前的序列为：")
    for i in lists:
        print(i, end=" ")
    print("\n排序后的序列为：")
    for i in quickSort(lists, 0, len(lists) - 1):
        print(i, end=" ")
