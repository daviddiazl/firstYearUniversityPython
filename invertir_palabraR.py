"""invertir una palabra en recursivo"""

def invertir_palabraR(palabra,pos=0):
    """int,str-->str
    OBJ:invertit palabra desde len(palabra) hasta pos
    PRE: 0<=pos<=len(palabra)"""
    p_invert=''
    if pos<len(palabra):
        p_invert= invertir_palabraR(palabra,pos+1)
        p_invert += palabra[pos]
    return p_invert

"""PROBADOR"""
print(invertir_palabraR('patata'))
print(invertir_palabraR('patata',3))