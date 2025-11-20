https://github.com/Raamia/lab11-RA-TR
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    try:
        if a<0:
            raise ValueError
        else:
            return math.sqrt(a)
    except:
        raise ValueError
def hypotenuse(a,b):
    try:
        return math.sqrt(((a**2)+(b**2)))
    except TypeError:
        return ValueError
def add(a, b): 
    return a+b
def subtract(a, b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a==0:
        raise ZeroDivisionError
    else:
        return b/a
def logarithm(a,b):
    if b<=0 or a<=0 or a == 1:
        raise ValueError
    else:
        return math.log(a,b)
def exp(a,b):
    return a**b