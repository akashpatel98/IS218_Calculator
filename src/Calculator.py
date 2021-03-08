from Operations.addition import addition
from Operations.multiplication import multiplication
from Operations.square import square
from Operations.subtraction import subtraction
from Operations.division import division
from Operations.square_root import square_root


def add(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def multiply(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c


def divide(a, b):
    a = int(a)
    b = int(b)
    c = a / b
    return c


def subtract(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c


def square(a, b):
    a = int(a)
    b = int(b)
    c = a ** b
    return c


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

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = square_root(a)
        return self.result
