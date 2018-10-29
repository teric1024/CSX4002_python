#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:25:36 2018

@author: user
"""

n = int(input())
ans = 1
for i in range(1, n+1):
    ans *= i
print(ans)