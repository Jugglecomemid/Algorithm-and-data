#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 12:53 PM
# @Author  : Charles He
# @File    : electiron_gate.py
# @Software: PyCharm


class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    def performGateLogic(self):
        pass


class BinaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter PinA for gate {} --> ".format(self.getLabel())))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter PinB for gate {} --> ".format(self.getLabel())))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("Error: No empty pins")


class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin for gate {} --> ".format(self.getLabel())))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: No empty pins")


class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()

        if a == 1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate  #可以返回传入的实例，因此其方法也能被调用

    def getTo(self):
        return self.togate



if __name__ == "__main__":
    g1 = AndGate("A1")
    g2 = AndGate("A2")
    g3 = OrGate("A3")
    g4 = NotGate("A4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


    # g1
    #    --> g3 --> g4
    # g2


