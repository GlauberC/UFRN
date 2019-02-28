def verifica(s, x, y):
    soma = x + y
    difx = s - x
    dify = s - y

    if (s % soma == 0):
        return True
    elif (difx % soma == 0):
        return True
    elif (dify % soma == 0):
        return True
    else:
        return False


s = int(input())
x, y = 2, 1
print(s, ':', sep='')
while (x <= s / 2 + 1):
    if (verifica(s, x, y)):
        print('{},{}'.format(x, y))
    if (x > y):
        y += 1
    else:
        x += 1

