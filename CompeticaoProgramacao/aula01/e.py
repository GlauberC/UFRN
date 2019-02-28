def questaoE():
    wA, wB = input().split()
    saida = 0
    temp = 0
    i = 0
    for l in wB:
        if (l == wA[i]):
            i += 1
            temp += 1
            if (temp > saida):
                saida = temp
        else:
            i = 0
            temp = 0
        if (i == len(wA)):
            return saida
    return saida


tests = int(input())
for test in range(0, tests):
    print(questaoE())