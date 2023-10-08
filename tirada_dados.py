"""Simular lanzamiento de dados con random randint"""

import bib_estadistica #biblioteca adjunta por el profesor
import random
import math

n_tiradas = 100
caras = (1,2,3,4,5,6)
#Tanto el n_tiradas como las caras del dado pueden variar dando igual una solucion 
total_caras = []
print('n_tirad', end ='\t')

cont = 0 
for n_cara in caras:
    total_caras = total_caras + [0]
    print(n_cara, end = '\t')
print('f_teorica','media','desv_tip','coef_var',sep='\t', end ='\t')

while cont < 4:
    for i in range(1,n_tiradas):
        sale = random.randint(1,len(caras))
        for j in caras:
            if sale == j:
                total_caras[j-1] += 1
    print()
    print(n_tiradas, end = '\t')
    for total in total_caras:
        print(total,end = '\t')
    print(bib_estadistica.media(total_caras),end='\t'*2)
    print(bib_estadistica.media(total_caras),end ='\t')
    print(round(bib_estadistica.desv_tipica(total_caras),2),end = '\t'*2)
    try:
        print(round(bib_estadistica.coef_var(total_caras),2),end = '\t') 
    except:
        print(bib_estadistica.coef_var(total_caras),end ='\t')
    #Debido a que en la biblioteca original adjuntada por el profesor al hacer el coef de var te devuelve un error
    #esto hace que no se puede redondear el coef var, para que quede exactamente como en el ejemplo y se pueda redondear
    #hay que modificar el return del coef_var para que solo te devuelva el valor numerico
    n_tiradas = n_tiradas *10
    cont += 1

#Decidimos no subprogramar debido a la poca probabilidad de volver a usar este programa 
# en gran parte debido a tocar la interfaz de usuario.

#Como conclusion, el que randint nos de diferentes valores a la hora de usar el programa con los mismos datos
#  no dificulta en nada el analisis cientifico, es mas lo aumenta, puesto que en un entorno aleatorio aun 
# teniendo los mismos datos no siempre dara los mismos resultados.

        