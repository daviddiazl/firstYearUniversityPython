"""Herramientas de dibujo grafico"""

from collections import namedtuple

#tColor = list de 3 0<=int<=255 orden RGB

tColor = namedtuple('color',['R','G','B'])
#int,int,int

def subida_intensidad(color,porcentaje):
    """tColor, float-->tColor
    OBJ: Oscurece color en porcentaje
    PRE: """
    for i in range(3):
        color[i] *=(1.0-porcentaje/100.0)
    
    return color 

"""PROBADOR"""
print(subida_intensidad([20,20,20],10))

def crea_color(r,g,b):
    """str-->tColor
    OBJ: Crea color 
    PRE:0<=r,g,b<=255"""
    return tColor(r,g,b)

print(crea_color(133,0,238))

