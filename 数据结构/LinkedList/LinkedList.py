#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 3:36 PM
# @Author  : Charles He
# @File    : LinkedList.py
# @Software: PyCharm


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext



class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)  # initial a value
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 假设第一个元素需要移除 那么就无移动了
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        temp = Node(item)
        current = self.head
        final = False
        while not final:
            if current.getNext() == None:
                final = True
            else:
                current = current.getNext()

        current.setNext(temp)


    def insert(self, pos, item):
        temp = Node(item)
        current = self.head
        previous = None

        if pos == 0:
            self.add(item)
        else:
            while pos > 0:
                previous = current
                current = current.getNext()
                pos -= 1

            previous.setNext(temp)  # 分别连接
            temp.setNext(current)


    def index(self, item):
        current = self.head
        count = 0

        while current.getData() != item:
            count += 1
            current = current.getNext()

        return count

    def pop(self):
        current = self.head
        previous = None
        final = False

        while not final:
            if current.getNext() == None:
                final = True
            else:
                previous = current
                current = current.getNext()

        previous.setNext(None)

        return current.getData()


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 假设第一个元素需要移除 那么就无移动了
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        # 遍历
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        # 假如插入第一位
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def index(self, item):
        current = self.head
        count = 0

        while current.getData() != item:
            count += 1
            current = current.getNext()

        return count

    def pop(self):
        current = self.head
        previous = None
        final = False

        while not final:
            if current.getNext() == None:
                final = True
            else:
                previous = current
                current = current.getNext()

        previous.setNext(None)
        return current.getData()

    # waiting
    def pop(self, pos):
        current = self.head
        previous = None
        later = None

        if pos == 0:
            previous = self.head
            self.head= current.getNext()
            return previous.getData()

        else:
            while pos > 0:
                previous = current
                current = current.getNext()
                later = current.getNext()
                pos -= 1

        previous.setNext(later)

        return current.getData()



if __name__ == "__main__":
    link_lst = UnorderedList()
    link_lst.add("1")
    link_lst.add('3')
    link_lst.add("4")

    link_lst.insert(2, "5")
    pop = link_lst.pop()

    print(link_lst.search("5"))
    print(link_lst.index("5"))
    print(pop)

    print("---------------------------")

    ord_lst = OrderedList()
    ord_lst.add(3)
    ord_lst.add(1)
    ord_lst.add(5)
    ord_lst.add(2)

    print(ord_lst.pop(pos=3))













