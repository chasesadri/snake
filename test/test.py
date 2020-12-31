import math
# -*- coding: utf-8 -*-
"""
Problem Set 0

Created on Thu Sep 10 17:15:44 2020

@author: chase

ASSIGNMENT:
    Write a program that...
    1. Asks the user to enter a number "x"
    2. Asks the user to enter a number "y"
    3. Prints out the number "x", raised to the power "y".
    4. Prints out the log (base 2) of "x"
"""

x = int(input('Enter number x: '))
y = int(input('Enter number y: '))

print('x to the power of y =', x**y)

print('log(x) =', math.log(x, 2))