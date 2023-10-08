"""recibe cadena, valida si nombre persona y formatea sus caracteres correctamente"""
CARACTERES_VALIDOS='QWERTYUIOPASDFGHJKLÑZXCVBNM '
def es_nombre_valido(nombre):
    """str-->error
    OBJ: si es nombre valido?
    PRE: caracteres validos ya asignado"""
    for letra in nombre:
        if letra.upper in CARACTERES_VALIDOS and len(nombre)<40:
            error = False
        else:
            error = True
    return error
            



def formatear_nombre(nombre):
    """str-->str
    OBJ:nombre formateado correctamente
    PRE: nombre valido"""
    cont=0
    nombre_correcto = ''
    for letra in nombre:
        if letra !=' ' and nombre[cont-1]!=' ':
            nombre_correcto+= letra.upper 
        elif letra!=' ':
            nombre_correcto+= letra
        elif nombre[cont]!=' ':
            nombre_correcto+= letra
        cont+=1
    return nombre_correcto

"""PROBADOR"""
print(formatear_nombre('albacete'))