# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 23:06:35 2018

@author: user
"""

n = input()
n = int(n)
dozen = n // 12
rest = n % 12
if rest == 0:
    print(dozen,"dozen")
else:
    print(dozen,"dozen and", rest)