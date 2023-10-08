"""Calcula la estacion del anno según mes y dia"""

def estaciones_anno(mes:int,dia: int) -> str:
    """ int*2--> str
    OBJ: Conocer la estacion del anno debido a mes y dia
    PRE: dia y mes fevhas validas """
    if  mes >=3 and mes<=6 and dia>=21:
        estacion= 'primavera'
    elif  mes >= 6 and mes<= 9 and dia>=21:
        estacion = 'verano'
    elif  mes >= 9 and mes <= 12 and dia>= 21: 
        estacion = 'otoño'
    else:
        estacion= 'invierno'

    return estacion

"""PRUEBA"""
print(estaciones_anno(3,20))
print(estaciones_anno(3,21))
print(estaciones_anno(6,20))


