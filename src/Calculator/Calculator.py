from Calculator.Operations.addition import addition
from Calculator.Operations.multiplication import multiplication
from Calculator.Operations.square import square
from Calculator.Operations.subtraction import subtraction
from Calculator.Operations.division import division
from Calculator.Operations.square_root import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def squaring(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = square_root(a)
        return self.result
