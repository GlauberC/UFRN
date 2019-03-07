#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:52:51 2019

@author: glauberc
"""

def rotateSquare(s, l):
    nS = []
    for j in range(l):
        q = []
        for i in range(l-1, -1 ,-1):
            q.append(s[i][j])
        nS.append(q)
    return nS

def isIn(i, j):
    for x in range(0, n):
        for y in range(0, n):
            if bS[i+x][j+y] != sS[x][y]:
                return False
    return True

n, N = 1, 1
while(n != 0 and N != 0):
    N, n = input().split()
    N, n = int(N), int(n)
    if(n != 0 and N != 0):
        bS = []
        sS = []
        for cN in range(N):
            bS.append(list(input()))
        for cN in range(n):
            sS.append(list(input()))
       
        for cont in range(4):
            soma = 0
            if cont > 0 :
                sS = rotateSquare(sS, n)
            for i in range(N):
                for j in range(N):
                    if(i <= N - n and j <= N - n):
                        if bS[i][j] == sS[0][0]:
                            if isIn(i, j):
                                soma += 1
            if(cont < 3):
                print(str(soma), end = ' ')
            else:
                print(soma)
     
                       

                
    

