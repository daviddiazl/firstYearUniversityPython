#Ejercicio 5 sesion 6
"""Construye un subprograma que devuelva la varianza de una población.
Presta atención a no pedir al ordenador más trabajo que el que harías a mano. """
 
def varianza(p):
    """list-->float
    OBJ: hallar varianza de poblacion
    PRE:           """
    n = len(p)
    sumatorio = 0
    for i in p:
        sumatorio += i
        med = sumatorio/n
         
    diferencia = 0
    for i in p:
        diferencia += (i-med)**2
        var= diferencia /(n-1)
    
    
    return var

print(varianza([1,2,3,4]))

