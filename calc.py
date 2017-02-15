from __future__ import division

class PolishCalc():
    def __init__(self):
        self.orig_problem = raw_input("numbers in front - spaces between - operator at end.> ").strip().split()
        self.operator = self.orig_problem.pop(-1)
        self.nums = self.orig_problem

    def do_maths(self):
        if self.operator in '+-/*':
            if self.operator == '+':
                print(self.addi())
            elif self.operator == '-':
                print(self.subt())
            elif self.operator == '/':
                print(self.divi())
            elif self.operator == '*':
                print(self.mult())

    def addi(self):
        answer = 0
        for num in self.nums:
            answer += int(num)
        return answer


    def subt(self):
        answer = 0
        for num in self.nums:
            answer -= int(num)
        return answer


    def mult(self):
        answer = 1
        for num in self.nums:
            answer *= int(num)
        return answer

    def divi(self):
        answer = int(self.nums[0])/int(self.nums[1])
        return int(answer)


problem = PolishCalc()
problem.do_maths()
