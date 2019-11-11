# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n= int(input("Input a natural number: "))
def squarenum(n):
    if n<= 0:
        print("Enter a positive number.")
    else:
        sum = 0
        temp = 1
    while temp <= n:
        sum += temp**2
        temp += 1
    return sum
print ("The sum of the square of first", n, "number(s) is/are: ", squarenum)
