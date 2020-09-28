#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 11:43 AM
# @Author  : Charles He
# @File    : 正则表达式转换成中文文本（递归）.py
# @Software: PyCharm


import re
import copy


class ReParse():
    def __init__(self, arr):
        self.pattern = arr
        self.result = []

    def split(self, pattern):
        """
        作用：
            切分形如这样的pattern：'(求其|是但|是旦|隨便)(哼|亨|唱|將){{一}首|{一}隻}歌{仔}{嚟}{比我|俾我}(聽|停)'
                        result=['(', '求其', '|', '是但', '|', '是旦', '|', '隨便', ')', '(', '哼', '|', '亨', '|', '唱', '|', '將', ')', '{', '{', '一', '}', '首', '|', '{', '一', '}', '隻', '}', '歌', '{', '仔', '}', '{', '嚟', '}', '{', '比我', '|', '俾我', '}', '(', '聽', '|', '停', ')']
        核心思想：
            转化成树结构（list实现）
        :param pattern:
        :return:
        """
        pt = re.compile(r'([\{\}\|\(\)])')
        arr = re.split(pt, pattern)
        arr = list(filter(lambda item: item != '', arr))
        return arr

    def findNext(self, str):
        """
        作用：
        把同等级的括号（'{'或者'(')找出来并切分
        :param str:
        :return:
        """
        str = list(str)
        if str[0] == '{':
            nextsign = '}'
        else:
            nextsign = ')'
        tempt = [str[0]]
        endPoint = -1
        for i in range(1, len(str)):
            if str[i] == str[0]:
                tempt.append(str[i])
            elif str[i] in nextsign:
                tempt.pop(-1)
            else:
                pass
            if len(tempt) == 0:
                endPoint = i
                break
        return str[:endPoint + 1], str[endPoint + 1:]

    def recur(self, left, present):
        """
        作用：
            递归切分为树结构
        :param left:
        :param present:
        :return:
        """
        if len(left) == 0:
            self.result = present
            return

        if left[0] == '{':
            lleft, rleft = self.findNext(left)
            present.append([' ', '|'])
            lleft.pop(0)
            self.recur(lleft, present[-1])
            self.recur(rleft, present)
        elif left[0] == '(':
            lleft, rleft = self.findNext(left)
            present.append([])
            lleft.pop(0)
            self.recur(lleft, present[-1])
            self.recur(rleft, present)
        elif left[0] == ')':
            pass
        elif left[0] == '}':
            pass
        elif left[0] == '|':
            present.append('|')
            self.recur(left[1:], present)
        else:
            present.append(left[0])
            self.recur(left[1:], present)

    def getResult(self, med, prearr):
        """
        作用：
        递归实现
        :param med:
        :param prearr:
        :return:
        """
        # 每次处理列表的一个元素
        # 可能是嵌套列表:返回该列表所有组合的集合(prearr),再与上一个函数的prearr结合，pop出med的当前项
        # 可能是字符串：prearr的每一项都添加该字符串
        if len(med) == 0:
            return prearr
        if type(med[0]) == type([]):
            prearrnext = []
            # 把"|"分隔的都抽出来各自处理
            division = []
            divisionindex = [-1]
            for i in range(len(med[0])):
                if med[0][i] == '|':
                    divisionindex.append(i)
            divisionindex.append(len(med[0]))
            for i in range(len(divisionindex) - 1):
                if divisionindex[i + 1] - divisionindex[i] > 2:
                    division.append(list(med[0][divisionindex[i] + 1:divisionindex[i + 1]]))
                else:
                    division.append(med[0][divisionindex[i] + 1])
            # 每个分隔符之间的内容分别递归，获得各自的值
            for divi in division:
                prearrnexti = self.getResult(divi, [])
                prearrnext.extend(prearrnexti)
            # 把合并后的div再和prearr的合并
            if len(prearr) == 0:
                for item in prearrnext:
                    prearr.append(item)
            else:
                prearrCopy = copy.deepcopy(prearr)
                prearr.clear()
                for itemi in prearrCopy:
                    for itemj in prearrnext:
                        prearr.append(itemi + itemj)
            med.pop(0)
            # 再继续处理后面的
            if type(med) == type([]) and len(med) != 0:
                prearr = self.getResult(med, prearr)
            return prearr
        else:
            if len(prearr) == 0:
                if type(med) == type([]):
                    prearr.append(med[0])
                else:
                    prearr.append(med)
            else:
                prearrCopy = copy.deepcopy(prearr)
                prearr.clear()
                for item in prearrCopy:
                    prearr.append(item + med[0])
            if type(med) == type([]) and len(med) != 0:
                med.pop(0)
                prearr = self.getResult(med, prearr)
            return prearr

    def Parse(self):
        arr = self.split(self.pattern)
        self.recur(arr,[])
        self.result = self.getResult(self.result, [])
        self.result = list(map(lambda a: re.sub(r' ', '', a), self.result))
        return self.result


if __name__ == "__main__":
    patterns = ['(我想知{道}|我想了解) $entityname::entity (今|上)个星期有几{多}人(好返|治愈|康复)']
    for i in range(len(patterns)):
        print("第%s个:\t" % i)
        result = ReParse(patterns[i]).Parse()  # 丢进去形如 '唱首(開心嘅|情)歌{俾我聽}'的string就出来一个list
        print(result)
