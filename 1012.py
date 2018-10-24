# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 23:10:13 2018

@author: user
"""

status = input()
score = input()
if status != 1 and status != 2:
    print("roll error")
elif score >= 0 and score <= 100:
    print("score error")
else:
    if status == 1 and score >= 60:
        print("pass")
    elif status == 2 and score >= 70:
        print("pass")
    else:
        print("fail")      