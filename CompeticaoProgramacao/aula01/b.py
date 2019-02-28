entrada = input()
for i in range(0,int(entrada)):
  n1, n2, n3 = input().split()
  n1 = int(n1)
  n2 = int(n2)
  n3 = int(n3)
  menor = min(n1, n2, n3)
  maior = max(n1, n2, n3)
  for n in [n1, n2, n3]:
    if n != menor and n != maior:
      print('Case {}: {}'.format(i+1, n))