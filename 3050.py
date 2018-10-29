#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:44:26 2018

@author: user
"""

n = int(input())
counter = 1
for i in range(1,n+1):
    for j in range(i):
        print(counter, end = " ")
        counter += 1
    print()

