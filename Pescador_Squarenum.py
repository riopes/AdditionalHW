# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

squarenum = int(input("Enter a value:"))
i = 1
sum = 0
while(i<= squarenum):
    sum = sum+(i**2)
    i = i+1
if i>= squarenum:
    print ("Sum of square is:",sum)