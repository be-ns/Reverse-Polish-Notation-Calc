class PolishCalc():
    def __init__(self):
        self.nums = []
        self.answer = 0
        self.operators = {}
        self.original_input = []
        self.input = raw_input("numbers in front - spaces between - operator at end.> ").strip().split()
        for items in self.input:
            if items in '+-*/':
                self.original_input.append(items)
            elif items in map(str, list(range(1,500000))):
                self.original_input.append(items)
        for idx, itm in enumerate(self.original_input):
            try:
                self.nums.append(int(itm))
            except ValueError:
                pass
            if itm in '+-/*':
                self.operators[itm] = idx

    def do_maths(self):
        for key, value in self.operators.items():
            if key == '+':
                (self.addi(value))
            elif key == '-':
                (self.subt(value))
            elif key == '/':
                (self.divi(value))
            elif key == '*':
                (self.mult(value))
            print(self.answer)

    def addi(self, value):
        idx_to_add = list(range(0,value))
        for idxs in idx_to_add:
            self.answer += (int(self.original_input[idxs]))
        return self.answer


    def subt(self, value):
        idx_to_add = sorted(list(range(0,value)))
        for idxs in idx_to_add:
            if idxs == 0:
                self.answer = (int(self.original_input[idxs]))
            else:
                self.answer -= (int(self.original_input[idxs]))
        return self.answer


    def mult(self, value):
        idx_to_add = sorted(list(range(0,value)))
        for idxs in idx_to_add:
            if idxs == 0:
                self.answer = (int(self.original_input[idxs]))
            else:
                self.answer *= (int(self.original_input[idxs]))
        return self.answer


    def divi(self, value):
        idx_to_add = sorted(list(range(0,value)))
        for idxs in idx_to_add:
            if idxs == 0:
                self.answer = (int(self.original_input[idxs]))
            else:
                self.answer = self.answer / (int(self.original_input[idxs]))
        return self.answer
