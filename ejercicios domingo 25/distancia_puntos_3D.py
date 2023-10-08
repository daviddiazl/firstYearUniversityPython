#ejercicio 8 cuaderno 2 
"""8.	Escribe una función que a partir de las coordenadas 3D de dos puntos en el espacio en formato (x, y, z)
 calcule la distancia que hay entre dichos puntos.  Prueba su función y el resultado por pantalla. """


def distancia_puntos(x1,y1,z1,x2,y2,z2):
    """float*6-->float
    OBJ:distancia entre dos puntos plano tridimensional
    PRE: Todos los valores deben de ser float"""
    import math
    distancia_puntos= math.sqrt((x1-x2)**2 +(y1-y2)**2 + (z1-z2)**2)
    
    return distancia_puntos

"""PROBADOR"""
print(distancia_puntos(1,1,1,2,2,2))#debe dar 1.732 aprox
print(distancia_puntos(0,0,0,2,2,2))#debe dar 3.464 aprox
print(distancia_puntos(4,-3,5,9,1,-25))# debe dar 30,675 aprox 

"""Una de las cosas que menos me covence de el programa es que se tenga que implementar librerias ajenas para
que la funcion funcione (como lo es math), podria resolverse utilizando un mecanismo para hacer raices cuadradas 
desde el programa."""