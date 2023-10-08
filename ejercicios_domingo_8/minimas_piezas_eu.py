#Ejercicio 14 cuaderno 3 sesion 6

"""14)	Haz un subprograma que indique la forma óptima de componer una determinada cantidad, usando las piezas 
acuñadas en el Sistema Monetario. Por óptima queremos decir formada por el mínimo número de piezas."""

piezas_eu = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

def monedero_optimo(sistema_monetario,dinero):
    """list,float-->list
    OBJ:organizar monedero optimo
    Pre: dinero >=0 """
    piezas = sistema_monetario
    for pieza in range(0,len(piezas)):
        division = (dinero/sistema_monetario[pieza])
        if division >=1:
            dinero = (division - int(division)) * sistema_monetario[pieza]
            piezas[pieza] = int(division)
        else:
            piezas [pieza] = 0

    return piezas



"""PROBADOR"""
print(monedero_optimo(piezas_eu,62765.55))
print(monedero_optimo(piezas_eu,35.15))
