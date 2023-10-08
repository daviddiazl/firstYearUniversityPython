"""*****************************       Bib_dinero       *************************************"""

UE = (500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01)

#tMondero=lista de enteros paralela a UE

def piezas_mon(monedero):
    """ tMonedero--> int
    OBJ: cuantas piezas en monedero
    PRE:"""

    cont = 0
    for n_piezas in monedero:
        cont+= n_piezas


    return cont