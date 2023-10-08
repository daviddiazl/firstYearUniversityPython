from collections import namedtuple

tPunto = namedtuple('punto','x, y')
#num,num
p= tPunto(20,20)
print(p)


tSegmento = namedtuple('segmento','pini, pfin')
#tPunto,tPunto

"""distancia entre puntos"""

def distancia(p1,p2):
    """tPunto*2-->num
    OBJ:distancia entre dos puntos
    PRE:"""
    from math import sqrt
    return sqrt((p1.x-p2.x)**2 +(p1.y-p2.y)**2)

p1 = tPunto(2,1)
p2 = tPunto(2,2)
seg1 = tSegmento(p1,p2)

"""PROBADOR"""
print(distancia(p1,p2))
print('el',seg1, 'mide %5.3f'%(distancia(seg1.pini,seg1.pfin)))

def tamanno (s):
   """ tSegmento-->float
   OBJ: tamaño del segmento s """
   return distancia(s.pini,s.pfin)

"""PROBADOR"""
print('el',seg1, 'mide %5.3f'%(tamanno(seg1)))                          

def punto_aleatorio():
    """nada--> tPunto
    OBJ: crea un punto aleatorio 0<=x,y<=1                   """
    from random import random
    x = random()
    y = random()
    return tPunto(x,y)

"""PROBADOR"""
print(punto_aleatorio())

def esta_en_circulo(p,r):
    """tPunto,float-->bool
     OBJ:True si punto p está dentro de circulo de radio
       con centro 0,0"""  
    return p.x*p.x + p.y*p.y <= r**2

"""PROBADOR"""
print(esta_en_circulo(punto_aleatorio(),3))