"""pintar un poligono """
from turtle import *

def pintar_poligono (v,tam):
    """ int,int-->
    OBJ : pintar poligono
    PRE: v>=3 """
    for lado in range(v+1):
        fd(tam)
        rt(360/v)

pintar_poligono(3,100)