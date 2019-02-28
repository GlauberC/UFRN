#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:03:19 2019

@author: glauberc
"""

#Entrada
"""
Madam, Im adam!
Roma tibi subito motibus ibit amor.
Me so hungry!
Si nummi immunis
DONE
"""

#Saída
"""
You won’t be eaten!
You won’t be eaten!
Uh oh..
You won’t be eaten!
"""

def isValidLetter(l):
    if(l < 97 or l > 122):
        return False
    else:
        return True

def isPali(p):
    pali = False
    j = len(p) - 1
    i = 0
    
    while (j > i):
        lBegin = ord(p[i].lower())
        lEnd = ord(p[j].lower())
        if(isValidLetter(lBegin) and isValidLetter(lEnd)):
            if(lBegin == lEnd):
                i+=1
                j-=1
            else:
                return False
        else:
            if(not isValidLetter(lBegin)):
                i+=1
            if(not isValidLetter(lEnd)):
                j-=1        
    return True

p = ' '
while(p != "DONE"):
    p = input()
    if(p != "DONE"):
        if isPali(p):
            print("You won't be eaten!")
        else:
            print("Uh oh..")