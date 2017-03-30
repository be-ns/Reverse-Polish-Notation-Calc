from collections import OrderedDict
import os
import sys


class PolishCalc(object):
    def __init__(self):
        '''
        initializes the stack
        '''
        self.answer = 0
        self.stack = []
        self.input = input('Numbers at the beginning > operator at the end> ').strip()
        self.maths = ['+','-','/','*']
        self.do_maths()


    def do_maths(self):
        # (self.stack).remove(0)
        self.input = [item for item in self.input.split(' ')]
        for item in self.input:
            if item not in self.maths:
                self.stack.append(int(item))
            else:
                if item == '+':
                    self.answer = self.add()
                elif item == '-':
                    self.answer = self.subtract()
                elif item == '/':
                    self.answer = self.divide()
                elif item == '*':
                    self.answer = self.multiply()
            # print(self.answer)
        print(self.answer)
        # ("The solution to your input is {0}.".format(self.answer))

    def add(self):
        self.answer = (sum(self.stack))
        self.stack = [self.answer]
        return(self.answer)

    def subtract(self):
        if self.answer == 0:
            self.stack.pop(0)
            for itm in self.stack:
                self.answer -= itm
            self.stack = [self.answer]
        else:
            self.stack.pop(0)
            self.answer -= (sum(self.stack))
            self.stack = [self.answer]
        return(self.answer)

    def divide(self):
        if self.answer == 0:
            self.answer = self.stack.pop(0)
            for itm in self.stack:
                self.answer = (self.answer / itm)
            self.stack = [self.answer]
            return(self.answer)
        else:
            self.answer = self.stack.pop(0)
            for itm in self.stack:
                self.answer = (self.answer / float(itm))
            self.stack = [self.answer]
        return(self.answer)

    def multiply(self):
        if self.answer == 0:
            self.answer = self.stack.pop(0)
            for itm in self.stack:
                self.answer = (self.answer * itm)
            self.stack = [self.answer]
            return (self.answer)
        else:
            self.answer = self.stack.pop(0)
            for itm in self.stack:
                self.answer *= itm
            self.stack = [self.answer]
        return(self.answer)

    def __repr__(self):
        return ("The solution to your input is {0}.").format(self.answer)

if __name__ == '__main__':
    calc = PolishCalc()
