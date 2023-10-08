import numpy as np
col = 0
fila = 0
n = 4
cont =0
try: 
    col = input()
    fila = input()
    print('\n')
except:
    print('Escriba un valor numerico') 
else:
    col = int(col)
    fila = int(fila)
    matriz = np.zeros((col,fila))
    while(cont < n):
        a_col = 0
        a_fil = 0
        try:
            a_col = input()
            a_fil = input()
            a_col = int(a_col)
            a_fil = int(a_fil)
            print('\n')
        except:
            print('Escriba un valor numerico')
        else:
            for i in range(0,a_col):
                for j in range(0,a_fil):
                    matriz[i][j] +=1
                    print(matriz[i][j])
        cont +=1


    