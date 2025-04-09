"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def logarithm(a, b):
    return math.log(b, a)


def hypotenuse(a, b):
    return a ** 2 + b ** 2


def sqrt(a):
    return math.sqrt(a)