# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
ng = 1
while(ng > 0 ):
    ent = input()
    if len(ent) > 1:
        ng, s = ent.split()
        ng = int(ng)
        size = int(len(s) / ng)
        
        j = 0
        temp = 0
        for i in range(len(s)):
            if i % size == 0:
                temp = i
                if i + size <= len(s):
                    j = temp + size - 1
            if j >= temp:
                print(s[j], end='')
                j -= 1
        print()
    else:
        ng = 0
        
       