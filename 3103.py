#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:22:11 2018

@author: user
"""

ans = int(input())
lowerb = 1
upperb = 100
input_value = 0

while True:
    print(lowerb, "< ? <", upperb)
    input_value = int(input())
    if input_value == ans:
        print("bingo answer is", ans)
        break
    else:
        print("wrong answer, guess", end = " ")
        if input_value < ans:
            print("larger")
            lowerb = input_value
        else:
            print("smaller")
            upperb = input_value