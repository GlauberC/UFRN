testes = int(input())
for test in range(0,testes):
    n, m = input().split()
    x = int(int(n) / 3)
    y = int(int(m) / 3)
    print(x*y)