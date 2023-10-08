"""Segun patrimonio calcular porcentaje"""

def porcent_imp_prog(patr):
    """num-->int
    OBJ: porcentaje segun patr
    PRE:"""
    if patr<1000000:
        impuesto = 0
    elif 1000000<=patr<=5000000:
        impuesto =1
    elif 5000000<patr<10000000:
        impuesto =2
    elif 10000000<=patr<40000000:
        impuesto=3
    else:
        impuesto=7


    return impuesto

"""PROBADOR"""
print(impuesto_prog(20000),'%')
print(impuesto_prog(3000000),'%')
print(impuesto_prog(7000000),'%')
print(impuesto_prog(20000000),'%')
print(impuesto_prog(50000000),'%')