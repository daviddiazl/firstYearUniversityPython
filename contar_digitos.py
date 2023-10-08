"""Contar los digitos de un numero"""

def numero_digitos(n):
    """int-->int
    OBJ: contar numero de digitos de n
    PRE: n>=0"""
    cont=0
    while n>0:
        cont+=1
        n = n//10
    return cont

print(numero_digitos(1220000))
print(numero_digitos(2))

"""contar digitos de un numero recursivo"""
def numero_digitosR(n,pos=0):
    """num,int-->int
    OBJ: contar num digitos
    PRE:"""
    digitos = 0
    if n <=0:
        digitos=0
    else:
        digitos = digitos + numero_digitosR(n//10)
        digitos +=1
    return digitos

"""PROBADOR"""
print(numero_digitosR(1220000))
print(numero_digitosR(10))