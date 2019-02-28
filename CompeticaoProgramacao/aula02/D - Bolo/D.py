#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:55:14 2019

@author: glauberc
"""

w = input()
while(w):
    w = int(w)
    n = int(input())
    
    area = 0
    for i in range(n):
        #entrada
        wi, li = input().split()
        area += int(li) * int(wi)
    
    print(int(area/w))
