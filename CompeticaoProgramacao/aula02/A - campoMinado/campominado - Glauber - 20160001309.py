field = 0
n, m = 1, 1
while(n != 0 or m != 0):
    n,m = input().split()
    n,m = int(n), int(m)
    if(n != 0 or m != 0):
   
        campoMinado= []
        field += 1
        if(field != 1):
            print()
            
        print('Field #{}:'.format(field))
        
        for i in range(0, n):
            l = input()
            campoMinado.append([])
            for q in range(0, m):
                if(l[q] == '.'):
                    campoMinado[i].append(0)
                else:
                    campoMinado[i].append('*')
        for i in range(0, n):
            for j in range(0, m):
                if (campoMinado[i][j] == '*'):
                    if(i != 0):
                        if campoMinado[i-1][j] != '*':
                            campoMinado[i-1][j] += 1    #cima
                    if(i != n-1):
                        if campoMinado[i+1][j] != '*':
                            campoMinado[i+1][j] += 1    #baixo
                    if(j != 0):
                        if campoMinado[i][j-1] != '*':
                            campoMinado[i][j-1] += 1    #esquerda
                    if(j != m-1):
                        if campoMinado[i][j+1] != '*':
                            campoMinado[i][j+1] += 1    #direita
                    if(i != 0) and (j != 0):
                        if campoMinado[i-1][j-1] != '*':
                            campoMinado[i-1][j-1] += 1  #cima esquerda
                    if(i != 0) and (j != m-1):
                        if campoMinado[i-1][j+1] != '*':
                            campoMinado[i-1][j+1] += 1  #cima direita
                    if(i != n-1) and (j != 0):
                        if campoMinado[i+1][j-1] != '*':
                            campoMinado[i+1][j-1] += 1  #baixo esquerda
                    if(i != n-1) and (j != m-1):
                        if campoMinado[i+1][j+1] != '*':
                            campoMinado[i+1][j+1] += 1  #baixo direita
        for i in range(0, n):
            for j in range(0, m):
                print(campoMinado[i][j], end='')
            print()