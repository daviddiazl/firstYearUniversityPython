#Ejercicio 3 

def votacion(lista):
    """lista--> str
    OBJ: ver si votacion unanime
    PRE: """

    respuesta = ''
    if False in lista:
        respuesta = 'no se cambia'
    else:
        respuesta = 'si se cambia'

    return  respuesta 

"""Pruebas"""
print(votacion([True,True,False]))
print(votacion([True,True,True]))
