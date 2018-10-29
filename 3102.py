#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:10:25 2018

@author: user
"""
import math
def isprime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n+1):
    if isprime(i):
        print(i, "is prime")