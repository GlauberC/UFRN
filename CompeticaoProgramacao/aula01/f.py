s = '0'
case = 1
while (s != ''):
    s = input()
    if (s != ''):
        queries = int(input())
        print('Case {}:'.format(case))
        for test in range(0, queries):
            n1, n2 = input().split()
            n1, n2 = int(n1), int(n2)
            menor = min(n1, n2)
            maior = max(n1, n2)
            intervalo = s[menor:maior + 1]
            char = s[menor]
            dif = maior - menor + 1
            test = dif * char
            if (intervalo in test):
                print('Yes')
            else:
                print('No')
        case += 1
