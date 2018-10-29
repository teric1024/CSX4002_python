#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:54:49 2018

@author: user
"""

n = int(input())
for i in range( (n-1)//2, 0, -1):
    for k in range(i):
        print(" ", end = "")
    for j in range(n - 2*i ):
        print("*", end = "")
    print()
        
for i in range(n):
    print("*", end ="")
print()

for i in range(1, (n+1)//2 ):
    for k in range(i):
        print(" ", end = "")
    for j in range(n - 2*i):
        print("*", end ="")
    print()