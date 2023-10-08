"""multiplicacion recursiva"""

def multiplicacion_enterosR(a,b):
    """2*int-->int
    OBJ:obtener mult de enteros con recursividad
    PRE:a y b >=0"""
    if a==0:
        mult=0
    elif a ==1:
        mult=b
    else:
        mult= b+multiplicacion_enterosR(a-1,b)
    return mult

"""PROBADOR"""
print(multiplicacion_enterosR(0,1))
print(multiplicacion_enterosR(1,1))
print(multiplicacion_enterosR(8,2))