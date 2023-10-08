tupla_prueba = (1,2,4,6,8)
from collections import namedtuple

def esta_sec(sec,elem):
    """sec de tElemento,tElemento-->bool
    OBJ: esta elem en sec?
    PRE: """
    pos=0
    while pos<len(sec) and elem != sec[pos]:
        pos+=1
    return pos<len(sec)

"""PROBADOR"""
print(esta_sec(tupla_prueba,1),' T')
print(esta_sec(tupla_prueba,8),' T')
print(esta_sec(tupla_prueba,3),' F')


def pos_sec(sec,elem):
    """sec de tElemento, tElemento-->int,error
    OBJ: buscar pos de elem en sec
    PRE:"""
    pos = 0
    while pos< len(sec) and elem != sec[pos]:
        pos+=1
    return pos, pos< len(sec)


"""PROBADOR"""
print(pos_sec(tupla_prueba,2))
print(pos_sec(tupla_prueba,0))

def pos_menor(sec,pos=0):
    """sec,int-->int
    OBJ: pos dato menor en secuencia
    PRE: pos<len(sec), len(sec)>0"""
    for i in range(pos+1,len(sec)):
        if sec[i]<sec[pos]:
            pos= i
    return pos

"""PROBADOR"""
print(pos_menor(tupla_prueba))
print(pos_menor(tupla_prueba,2))



def lista_ordenada(lista):
    """lista-->nada
    OBJ: ordena la lista 
    PRE:"""
    for pos in range(len(lista)-1):
        menor = pos_menor(lista,pos)
        lista[pos],lista[menor] = lista[menor],lista[pos]

"""PROBADOR"""
lista_prueba = [56,33,1,9,17]
lista_ordenada(lista_prueba)
print(lista_prueba)

def pos_binaria(sec,elem):
    """sec de tElem, tCampo --> int,error
    OBJ: posicion del elem con valor elem en campo en la sec y dice\
        si esta elem
    PRE: sec ordenada por Campo"""
    ini=0
    fin= len(sec)
    medio=(ini+fin)/2
    while ini<fin and sec(medio).campo!= elem:
        if sec(medio).campo>elem:
            fin=medio-1
        else:
            ini=medio+1
        medio=(ini+fin)/2
    return medio, ini==fin and sec(medio).campo!= elem

"""PROBADOR"""
