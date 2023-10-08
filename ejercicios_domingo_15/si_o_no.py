#Ejercicio 5 

def confirmacion_pedida(preg):
    """str-->bool
    OBJ:pide confirmacion al usuario con pregunta preg
    PRE: """
    respuesta = input(preg).upper()
    afirmacion = ['SI','YES','Y','OUI','T','ACEPTAR','CLARO']
    negacion = ['NO','N','NE','F','CANCELAR','NUNCA']
    while not ((respuesta in afirmacion) or (respuesta in negacion)):
        respuesta = input(preg).upper()
    
    return respuesta in afirmacion

"""PROBADOR"""
print(confirmacion_pedida('¿Tienes 18?: '))

#Este subprograma iria en una biblioteca 
# utilizada para su uso en interacciones con el usuario 
