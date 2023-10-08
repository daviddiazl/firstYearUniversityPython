#Programa para calcular si numero no es primo 



def teorema_wilson(n):
    """int-->bool
    OBJ: saber si no primo
    PRE:
    """
    from math import factorial
    return (factorial(n-1)%n)-n==(-1)


"""PROBADOR"""

print(teorema_wilson(32))



