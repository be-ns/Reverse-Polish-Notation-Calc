class PolishCalc():
    def __init__(self):
        self.answer = 0
        self.stack = []
        self.input = list(raw_input("numbers in front - spaces between - operator at end.> ").strip())

    def do_maths(self):
        for item in self.input:
            if item in map(str, list(range(1,500000))):
                self.stack.append(int(item))
            elif item in '+-*/':
                if item == '+':
                    self.addi()
                elif item == '-':
                    self.subt()
                elif item == '/':
                    self.divi()
                elif item == '*':
                    self.multi()
            else:
                pass
        return(self.answer)

    def addi(self):
        for itm in self.stack:
            self.answer  += itm
        self.stack = [self.answer]
        return self.stack

    def subt(self):
        if self.answer == 0:
            self.answer = self.stack[0]
            self.stack.pop(0)
            for itm in self.stack:
                self.answer -= itm
            self.stack = [self.answer]
        else:
            self.stack.pop(0)
            for itm in self.stack:
                self.answer -= itm
            self.stack = [self.answer]
        return self.stack

    def divi(self):
        if self.answer == 0:
            self.answer = self.stack[0]
            self.stack.pop(0)
            for itm in self.stack:
                self.answer = self.answer / itm
            self.stack = [self.answer]
        else:
            self.stack.pop(0)
            for itm in self.stack:
                self.answer = self.answer / itm
            self.stack = [self.answer]
        return self.stack

    def multi(self):
        if self.answer == 0:
            self.answer = self.stack[0]
            self.stack.pop(0)
            for itm in self.stack:
                self.answer = self.answer * itm
            self.stack = [self.answer]
        else:
            self.stack.pop(0)
            for itm in self.stack:
                self.answer = self.answer * itm
            self.stack = [self.answer]
        return self.stack



problem = PolishCalc()
print(problem.do_maths())
