#posicion de un elemento en un array

def posicion_array(sec,elem):
    """sec de tipo, tipo-->int
    OBJ:Posicion elemento en secuencia
    PRE:"""
    pos=0
    while pos<len(sec) and sec[pos]!=elem:
        pos+=1
    if pos<= len(sec) : 
        pos=-1

    return pos