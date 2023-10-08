"""Fuerza a partir de masa y aceleración"""

"""Implementa una función "fuerza" que retorne el valor de 
la magnitud física fuerza a partir de los valores de masa y 
aceleración recibidos como parámetros. Construye después un
 programa probador especificando los casos de prueba necesarios
  que muestre por pantalla el valor de la fuerza a partir de una
   masa y aceleración dadas. """

def fuerza(M,A):
    """
    fload--> fload 
    OBJ: conseguir F debido a M y A 
    PRE:M y A = fload , m>=0"""
    return M*A

"""PROBADOR"""
print(fuerza(200,3.4)) 
print(fuerza(0,0))
print(fuerza(200,-2.6))


