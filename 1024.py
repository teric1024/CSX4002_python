#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:23:39 2018

@author: user
"""

n = int(input())

for i in range(n-1):
    print(" ", end = "")
print("*")

for i in range(1, n-1):#print all groups
    for l in range(n-i, n-i-3, -1):#print a group
        for k in range(l, 0, -1):#print spaces
            print(" ", end = "")
        for j in range(2*(n-l)-1):#print leaves
            print("^", end = "")
        print()
        
for i in range(n-2):#print trunk
    for j in range(int(n/2+1/2)):
        print(" ", end = "")
    for k in range(n-2):
        print("#", end = "")
    print()