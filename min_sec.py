def pos_menor(sec,pos=0):
    """sec,int-->int
    OBJ: pos dato menor en secuencia
    PRE: pos<len(sec), len(sec)>0"""
    for i in range(pos+1,len(sec)):
        if sec[i]<sec[pos]:
            pos= i
    return pos

"""PROBADOR"""
tupla = (1,2,4,3)
print(pos_menor(tupla))
print(pos_menor(tupla,2))