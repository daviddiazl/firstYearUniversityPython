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



#ejercicio 5 cuaderno 3 sesion 5 
""" Una fábrica funciona ininterrumpidamente (7días*24horas). Se desea calcular el tiempo, 
expresado en horas y minutos, que ha trabajado un empleado, sabiendo el momento de entrada y
el de salida (expresados en horas y minutos). Un trabajador no puede trabajar más de 8 horas seguidas, 
de modo que el momento de entrada y el de salida, corresponden al mismo día (si entrada <= que la salida)
o a días consecutivos (en caso contrario). El programa indicará las horas y minutos trabajadas y caso de haber
trabajado más de 8 horas, dará una alerta.
¿puede que otra aplicación necesite algo que se calcule igual que el tiempo trabajado? 
Si fuera así, subprográmalo generalizándolo ¿Debes subprogramar la alerta, si el tiempo es mayor que un número
de horas? En todo caso, no lo mezcles en el mismo subprograma. Cada subprograma debe resolver un solo problema,
de lo contrario es menos reusable ¿Es responsabilidad del subprograma que las horas y minutos sean correctos, 
o por el contrario es una precondición?
Estas 2 afirmaciones dicen lo mismo: “min<60” o “min<=59” 
¿Cuál es más legible en la documentación del subprograma (docstring)?
"""


def tiempo_invertido(he,me,hs,ms):
    """int*4-->int*2
    OBJ: tiempo invertido desde la he y me hasta hs y ms 
    PRE:0<=he,hm<=23,0<= me,ms<=59"""

    if (he<=hs and me<=ms):
        tiempo_total = (hs-he),(ms-me)
    elif (he<hs and me>ms):
        me = 60 - me  
        tiempo_total = ((hs-he)-1),(me+ms)
    elif (he==hs and me>ms):
        tiempo_total = (23 , 60-(me-ms))
    elif (he>hs and me<=ms):
        he = 24-he
        tiempo_total = (he+hs,ms-me)
    else:
        he = 24 - he
        me = 60 - me
        tiempo_total = ((he+hs)-1,me+ms)
        
    return tiempo_total

def al_tiempo(tiempo):
    if tiempo[0]>8 :
        print('ALERTA, el trabajador ha trabajado mas de 8 horas')
        print('total de horas trabajadas: ',tiempo[0], ',total de minutos trabajados: ',tiempo[1])
    else:
        print('total de horas trabajadas: ',tiempo[0], ',total de minutos trabajados: ',tiempo[1])


"""PROBADOR"""
print(al_tiempo(tiempo_invertido(11,0,11,15)))
print(al_tiempo(tiempo_invertido(12,33,20,33)))
print(al_tiempo(tiempo_invertido(12,30,14,15)))
print(al_tiempo(tiempo_invertido(23,13,2,13)))
print(al_tiempo(tiempo_invertido(23,55,2,15)))
print(al_tiempo(tiempo_invertido(1,45,1,0)))
print(al_tiempo(tiempo_invertido(6,15,19,30)))
print(al_tiempo(tiempo_invertido(10,55,10,30)))



#ejercicio 4 cuaderno 3 sesion 6

"""Completa la interfaz del siguiente subprograma y su probador (con todos los casos de prueba requeridos):"""

def media(p):
    """sec(num) -->float
    OBJ: media de la población p
    PRE:  len(p)>0                    """  
    sumatorio = 0
    for i in p:
        sumatorio += i
        med = sumatorio/(float(len(p)))
    return med



#PROBADOR
print('Media de',[16,32,44,57,11],'debe dar: ',media([16,32,44,57,11]))
print('Media de',[-11,32,-6,-26,11],'debe dar: ',media([-11,32,-6,-26,11]))
print('Media de',[11,32.5,6.63,-26.9,11],'debe dar: ',media([11,32.5,6.63,-26.9,11]))


#Ejercicio 5 sesion 6
"""Construye un subprograma que devuelva la varianza de una población.
Presta atención a no pedir al ordenador más trabajo que el que harías a mano. """
 
def varianza(p):
    """list-->float
    OBJ: hallar varianza de poblacion
    PRE:           """
    n = len(p)
    sumatorio = 0
    for i in p:
        sumatorio += i
        med = sumatorio/n
         
    diferencia = 0
    for i in p:
        diferencia += (i-med)**2
        var= diferencia /(n-1)
    
    
    return var

print(varianza([1,2,3,4]))





#Ejercicio 14 cuaderno 3 sesion 6

"""14)	Haz un subprograma que indique la forma óptima de componer una determinada cantidad, usando las piezas 
acuñadas en el Sistema Monetario. Por óptima queremos decir formada por el mínimo número de piezas."""

piezas_eu = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

def monedero_optimo(sistema_monetario,dinero):
    """list,float-->list
    OBJ:organizar monedero optimo
    Pre: dinero >=0 """

    for pieza in range(0,len(sistema_monetario)):
        division = (dinero/sistema_monetario[pieza])
        if division >=1:
            dinero = (division - int(division)) * sistema_monetario[pieza]
            sistema_monetario[pieza] = int(division)
        else:
            sistema_monetario [pieza] = 0

    return sistema_monetario



"""PROBADOR"""
print(monedero_optimo(piezas_eu,62765.55))



"""


	                         David Díaz López         David Barrientos de Marco	           Miguel Hernandez Lozano
Horas trab. personal
 de FP sem: 26/10-1/11			5                               3                                     2

Horas TP de
 FP semana 1-8/11			    6                                4                                     4


David Díaz 			                                             9                                      7


David Barrientos 	            10                                                                       8		


Miguel Hernandez		        10                               10	
"""