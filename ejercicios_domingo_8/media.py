#ejercicio 4 cuaderno 3 sesion 6

"""Completa la interfaz del siguiente subprograma y su probador (con todos los casos de prueba requeridos):"""

def media(p):
    """sec(num) -->float
    OBJ: media de la población p
    PRE:  len(p)>0                    """  
    sumatorio = 0
    for i in p:
        sumatorio += i
        med = sumatorio/(float(len(p)))
    return med



#PROBADOR
print('Media de',[16,32,44,57,11],'debe dar: ',media([16,32,44,57,11]))
print('Media de',[-11,32,-6,-26,11],'debe dar: ',media([-11,32,-6,-26,11]))
print('Media de',[11,32.5,6.63,-26.9,11],'debe dar: ',media([11,32.5,6.63,-26.9,11]))