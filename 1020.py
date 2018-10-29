#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:13:12 2018

@author: user
"""

x = int(input())
ans = x
while x >= 3:
    ans += 1
    x -= 3
print(int(ans))