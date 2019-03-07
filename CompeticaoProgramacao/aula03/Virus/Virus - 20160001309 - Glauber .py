#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
while True:
  try:
    nC = 0
    nC = int(input())
    entrada = []
    ent = []
    ent = input().split()
    for e in ent:
        entrada.append(int(e))
    entrada.sort()
    j = nC - 1
    soma = 0
    for i in range(math.ceil(nC/2)):
        soma += entrada[j] - entrada[i]
        j -= 1
    print(soma)
  except EOFError:
    break