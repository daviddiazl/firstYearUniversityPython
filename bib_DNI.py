"""Perdon por los fallo ahora se podra ver mejor"""

"""Ejercicios recuperacion navidad 30/12/2020 """
"""Autor: David Díaz López"""


"""cuaderno 3 sesion 7 ejercicio 17"""

"""comprobar si DNI valido"""

def es_dni_valido(dni):
    """str-->error,bool
    OBJ: si DNI valido?
    PRE:"""

    LETRA_DNI_VALIDA='TRWAGMYFPDXBNJZSQVHLCKE'
    potencia=10**7
    total=0
    for i in range (0,8):
        try:
            n_dni= int(dni[i]*potencia)
        except:
            error = True 
            total ==0
        else:
            error = False
            potencia = potencia/10
            total += n_dni
    

    return error,(LETRA_DNI_VALIDA[total%23] == dni[8])

"""PROBADOR"""
print(es_dni_valido('49229064W'),' T')
print(es_dni_valido('41559467W'),' F')



"""cuaderno 3 sesion 7 ejercicio 18"""
"""subprograma que pida el dni al usuario hasta dni valido

def pedir_dni():
    int,str-->tupla,bool
    OBJ: pedir dni hasta DNI valido
    PRE:
    n_dni= int(input('Escriba su numero de DNI: '))
    letra_dni= input('Escriba su letra de DNI: ')
    dni=(n_dni,letra_dni)
    dni_valido= es_dni_valido(n_dni,letra_dni)
    while not dni_valido:
        n_dni= int(input('Escriba su numero de DNI: '))
        letra_dni= input('Escriba su letra de DNI: ')
        dni=(n_dni,letra_dni)
        dni_valido= es_dni_valido(n_dni,letra_dni)
    return dni,dni_valido

PROBADOR
print(pedir_dni())"""