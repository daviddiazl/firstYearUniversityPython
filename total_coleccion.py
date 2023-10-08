"""Cuaderno 3 sesion 6 ejercicio 2"""

"""Calcular precio total de coleccion completa"""

EDICION=(500.0,200.0,100.0,50.0,20.0,10.0,5.0,2.0,1.0,0.5,0.2,0.1,0.05,0.02,0.01)

def precio_coleccion(col):
    """tupla-->float 
    OBJ: precio coleccion completa
    PRE:"""
    total=0
    for pieza in col:
        total += pieza
    return total

"""PROBADOR"""
print(precio_coleccion(EDICION))