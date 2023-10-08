"""Suma pares desde 0 a n"""

def suma_paresR(n):
    """int--->int
    OBJ:Sumar los pares desde 0 a n
    PRE:n>=0"""
    if n ==0:
        suma=0
    elif n%2==0:
        suma=n+suma_paresR(n-2)   
    else:
        suma=suma_paresR(n-1)
        
    return suma

"""PROBADOR"""
print(suma_paresR(10))
print(suma_paresR(0))
print(suma_paresR(3))
