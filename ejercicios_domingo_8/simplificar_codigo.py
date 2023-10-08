#ejercicio 1 cuaderno 3 sesion 5
"""Los siguientes códigos, aunque hacen lo que se deseaba hacer, contienen errores conceptuales.
 Corrígelos y justifica tu propuesta. 

# 1 PRE: #0<=edad<=120         
if edad>=18:                        #quitamos el if edad>=0 ya que esta especificado en las PRE 
    es_mayor_edad=True
else: 
    es_mayor_edad=False          

#2 PRE: es_mayor_edad es bool
if es_mayor_edad==True:
    print('puede entrar en disco') 
else:
    print ('no puede entrar')
 
#3 PRE: 0<=n<=3   
j = 2**n                     #se puede escribir sin utilizar if con esta formula y el resultado seria igual
 
#4 PRE x,y,z inicializados. and tiene prioridad sobre or en Python 
if x==y and x==z:
     print('los 3 son iguales')       #eliminamos 1 igualdad ya que no es significante debido a las otras 2
elif x==y and y!=z or y==z and x!=y or x==z and x!=y:
    print('hay dos iguales')
else:                                 #ponemos else ya que ahorramos hacer operaciones innecesarias
    print('ninguno igual')

#5 0<=edad<=120 
if edad<=0 and edad<=13:       #quitamos el if edad<=0 ya que especifica en el PRE que tiene que ser mayor o igual
    print('niño')   
elif edad>13 and edad<18: 
    print('puber')
else:                      #borramos el anterior else ya que se especifica en el PRE los limites de edad
    print('adulto')
    
#6
    nombre= (input('teclee su nombre'))  #borramos el TRY, except y str, ya que cuando se quiere poner un string
                                         #es en el unico momento en el que se puede prescindir del try ya que el 
                                         # programa no aborta, quitamos el str ya que
                                         #input de serie el dato que recive es un string

#7
try:
    n=int(input('teclee un numero entero en cifras'))    #implementamos el try ya que lo que se busca recibir es un
                                                            #entero y no una cadena
except:
    print('Por favor ponga el valor en numerico')


#8 a inicializado a entero    
if a>=1:                             #distingimos la variable encontrado de ambos  y cambiams el if para
                                     #que se distinga entre un entero y otro que no lo es como por ejemplo un float
    a+=4
    encontrado=True
    print(a)
else:
    encontrado= False
    a+=2
    print(a)"""
