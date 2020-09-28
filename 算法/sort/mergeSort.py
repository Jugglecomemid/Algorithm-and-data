#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 5:23 PM
# @Author  : Charles He
# @File    : mergeSort.py
# @Software: PyCharm


def mergeSort(alist):
    print("Splitting: " + str(alist))
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2

    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    # 都分成长度为1 就返回出口 到下一步的merge
    # 之前某一部分分成1，则需要等待后续完成

    return merge(left, right)


def merge(left, right):
    print("Merging: " + str(left) +str(right))
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


if __name__ == '__main__':
    seq = [5, 3, 0, 6, 1, 4]
    print('排序前：', seq)
    result = mergeSort(seq)
    print('排序后：', result)
