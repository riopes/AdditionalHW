# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Squares = int(input("Enter a value:"))
i = 1
sum = 0
while(i<=Squares):
    sum = sum+(i**2)
    i = i+1
if i>= Squares:
    print ("Sum of square is:",sum)