#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:18:11 2018

@author: user
"""

n = int(input())
ans = n/2*(n+1)
for i in range(1,n):
    print(i,"+",sep = "", end ="")
print(n, "=", int(ans))