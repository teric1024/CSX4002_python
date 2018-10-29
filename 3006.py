#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:20:29 2018

@author: user
"""

n = int(input())
x = 0
if n >= 95:
    x = 2000
elif n >= 90:
    x = 1000
elif n >= 80:
    x = 500
else:
    x = 0
print("獎金",x, "元")