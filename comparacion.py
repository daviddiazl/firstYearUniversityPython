#Comparar dos numeros e imprime el mayor

try:
    numero_uno= float(input('Escriba el primer numero:'))
    numero_dos= float(input('Escriba el segundo numero:'))
except:
    print('Debe ser un valor numerico')
else:
    if numero_uno>numero_dos:
        print(numero_uno)
    elif numero_uno<numero_dos:
        print(numero_dos)
    else:
        print('iguales: ', numero_uno)
        #Mínimo numero de operaciones que necesitas= 1.
        # Maximo = 2
        # Promedio = 1.66 = (33+66*2)/99 
