entrada = int(input())
for i in range(0,entrada):
  n1,n2 = input().split()
  if int(n1) > int(n2):
    print('>')
  elif int(n1) < int(n2):
    print('<')
  else:
    print('=')