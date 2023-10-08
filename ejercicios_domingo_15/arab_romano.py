#Ejercicio 15

N_ROM= ('M',  'D','C','L','X','V','I')
VAL_R= (1000, 500,100,50, 10, 5,   1)
def arabico_romano(n):
    """int-->str
    OBJ: Convertir arabico a romano
    PRE: 1<=n<=3999  """
    
    romano=''
    pos=0
    while n >0:
        numero=int(n/VAL_R[pos]) 
        n=n%VAL_R[pos]
        if numero<=3: 
            romano+=N_ROM[pos]*numero
        elif  len(romano)>0 and romano[-1]==N_ROM[pos-1]:
            romano=romano[:-1]+N_ROM[pos]+N_ROM[pos-2]
        else: 
            romano=romano+N_ROM[pos]+N_ROM[pos-1]  
        pos+=1
    return romano

"""PRUEBAS"""
print(arabico_romano(3777))
print(arabico_romano(9))
#Este subprograma iria en una biblioteca matematica
#  o en una exclusivamente sobre conversiones