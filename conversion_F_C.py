#Ejercicio 10

"""Escribe un programa que utilizando un cierto valor de temperatura en grados Fahrenheit,
muestre en pantalla la temperatura equivalente en grados Centígrados. """

try:
    grados_f = float(input('Grados Fahrenheit: '))
except:
    print('Por favor escriba el valor en numerico')
else:
    grados_c = 5*(grados_f-32)/9
    print(grados_c,' grados Centigrados')
