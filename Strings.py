"""Strings"""
My_STR = 'Hello world'
print(dir(My_STR))#El metodo dir expone lo que puedes hacer con variable

print(My_STR.upper())#.upper() escribe las palabras en mayusc
print(My_STR.lower())#.lower() escribe las palabras en minusc
print(My_STR.swapcase())#.swapcase() cambia mayusc <--> minusc
print(My_STR.capitalize())#.capitalize() escribe primera letra en mayusc
print(My_STR.replace('Hello', 'Bye'))#.replace('a','b')reemplaza palabras
print(My_STR.replace('Hello', 'Bye').upper())#Se pueden convinar metodos
print(My_STR.count('l'))#Cuenta(en este caso las veces que esta l escrita)
print(My_STR.startswith('Hello'))#para saber si empieza con una palabra/letra determinada
print(My_STR.endswith('world'))#igual que startwith pero al final
print(My_STR.split())#Separa el texto
print(My_STR.find('o'))#Busca un determinado valor o letra
print(len(My_STR))#Entrega la longitud de la cadena, flotamte, array....
print(My_STR.index('e'))#Devuelve la posicion/indice de la letra palabra que buscamos
print(My_STR.isnumeric())#Para saber si es numerico
print(My_STR.isalpha())#Para saber si es alfanumerico
print(My_STR[4])#En str busca el digito que haya en la posicion 
print(f'My name is {My_STR}')

for car in 'tuputamadre':
    print(car)