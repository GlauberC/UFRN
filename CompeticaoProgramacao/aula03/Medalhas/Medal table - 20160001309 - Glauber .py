#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:20:42 2019

@author: glauberc
"""


#ler todos os valores
paises = []
np = int(input())
for ent in range(np):
    nome, o, p, b = input().split()
    paises.append([nome, int(o), int(p), int(b)])

# ordenar
for i in range(np):
    for j in range(i+1, np):
        if paises[i][1] < paises[j][1]:
            paises[i], paises[j] = paises[j], paises[i]
        elif paises[i][1] == paises[j][1]:
            if paises[i][2] < paises[j][2]:
                paises[i], paises[j] = paises[j], paises[i]
            elif paises[i][2] == paises[j][2]:
                if paises[i][3] < paises[j][3]:
                    paises[i], paises[j] = paises[j], paises[i]
                elif paises[i][3] == paises[j][3]:
                    if paises[i][0] > paises[j][0]:
                        paises[i], paises[j] = paises[j], paises[i]

#print ordem
for i in range(np):
    print("{} {} {} {}".format(paises[i][0], paises[i][1], paises[i][2], paises[i][3]))
    
