# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = input().split()
for i in range(len(n)):
    n[i] = eval(n[i])
c = (4*n[0] - n[1])/2
r = n[0] - c
if (n[1]%2 == 1 or c < 0 or r < 0):
    print("NO")
elif (n[1] <= 0 or n[0] <= 0):
    print("NO")
else:
    print("YES")
    print(int(c), int(r))