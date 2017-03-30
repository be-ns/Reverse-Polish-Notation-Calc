from operator import add, mul, sub, truediv


class PolishCalc(object):
    def __init__(self):
        '''
        initializes the stack
        '''
        self.stack = []
        self.input = input('Numbers at the beginning > operator at the end> ').strip()
        self.maths = ['+', '-', '/', '*']
        self.do_maths()

    def do_maths(self):
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
        print(self.answer)

    def add(self):
        self.stack.append(add(self.stack.pop(), self.stack.pop()))
        return(self.stack)

    def subtract(self):
        self.stack.append(sub(self.stack.pop(-2), self.stack.pop()))
        return(self.stack)

    def divide(self):
        self.stack.append(truediv(self.stack.pop(-2), float(self.stack.pop())))
        return(self.stack)

    def multiply(self):
        self.stack.append(mul(self.stack.pop(), self.stack.pop()))
        return(self.stack)

    def __repr__(self):
        return "The solution to your input is {0}.".format(self.answer)

if __name__ == '__main__':
    calc = PolishCalc()
