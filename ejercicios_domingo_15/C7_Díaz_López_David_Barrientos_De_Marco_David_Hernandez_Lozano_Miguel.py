#Ejercicio 2

x = 0
y = 1
inc = 0.1
#1 x,y,inc inicializados a float inc<<x<y. 
while x<y:
    x+=inc
    print(x) 
#Cambiamos != por < para que no de problemas 
#Si no le ves problemas, pruébelo con x=0, y=1, inc=0.1 
   
    
"""  
#2 VALOR es una constante, loquesea()
#  es una función definidas en la pieza llamante

def mi_fun(n):
    for i range (n):         #Borramos la variable r ya que es innecesaria 
                                        #pues vale lo mismo que loquesea
        if loquesea(i)>VALOR: return i
"""

i= 0
f= 10
#3 i, f inicializados a enteros

while i<f:
    print(i) 
    i+=3    
#Quitamos n pues vale lo mismo que i


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
print(arabico_romano(3000))
print(arabico_romano(321))
#Este subprograma iria en una biblioteca matematica
#  o en una exclusivamente sobre conversiones


"""
	                    David Diaz  	David Barrientos    	Miguel Hernandez
Horas TP de FP              4                   2                       1
semana 8-15/11

David Diaz                   8                  5                       5

			
Alumno 2                     8                  6                       5


Alumno 3                     8                  6                       5


"""