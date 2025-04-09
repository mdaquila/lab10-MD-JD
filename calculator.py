# https://github.com/mdaquila/lab10-MD-JD
# Partner 1: Matthew D'Aquila
# Partner 2: Joshua Dionne

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or input for logarithm.")
    return math.log(b, a)

def exp(a, b):
    return a ** b
