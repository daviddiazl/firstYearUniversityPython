#Ejercicio 12 cuaderno 1 

"""12.	El salario base de un vendedor es de 2.000 euros mensuales.
 A este salario se le suma un 3% de comisión sobre el total de las ventas que ha realizado,
  pero al total obtenido hay que descontarle un 32% del IRPF. Escribe un programa que, 
  a partir del importe de las ventas que ha realizado el vendedor durante el último mes y escriba 
  el salario neto que cobrará ese mes."""

try:
    dinero_ventas= float(input('Dinero en ventas el ultimo mes: '))
except:
    print('Por favor escriba el dato en numerico')
else:
    dinero_total_bruto = dinero_ventas*0.03 + 2000
    dinero_total = dinero_total_bruto*0.68

    print('El salario neto del trabajador es: ',dinero_total)






#Ejercicio 14 cuaderno 1 
#En python es posible hacer operaciones con variables str. Vamos a probarlo tecleando:
fruta ='ciruela'
tipo ='claudia'
print(fruta+tipo)
#ciruelaclaudia
 #a) ¿Qué se obtiene?¿Qué es lo que hace la operación + con las cadenas de texto?
"""Cuando tecleas esa operación tipo str. Y le das a la tecla "enter",
obtienes en una misma linea la fruta junto con su tipo, que en este caso es "ciruelaclaudia",
pero si lo cambias por otro significado, ambas, pues te dará un resultado diferente.Esta operación
lo que hace es juntar en una misma línea lo que se encuentra tanto delante como detrás del "+", 
que en este caso es fruta y tipo, pero si los cambias obtendrías otra solución."""
print (fruta*3)
#ciruelaciruelaciruela
 #b) ¿Qué se obtiene?¿Qué hace la operación * con los valores tipo texto?#
"""Al escribir esa operación lo que se obtiene es "ciruelaciruelaciruela", 
es decir tres veces el significado que le hemos puesto a fruta.
Si hubiesemos puesto otro significado pues obtendríamos otra solución.Lo qu ehace esta operación
con "" es la obtención de lo que pongas en el comando, tantas veces como le pongas detrás de "",
es decir, si le pones 5 veces pues aparecerá repetido lo mismo 5 veces."""






#ejercicio 8 cuaderno 2 
"""8.	Escribe una función que a partir de las coordenadas 3D de dos puntos en el espacio en formato (x, y, z)
 calcule la distancia que hay entre dichos puntos.  Prueba su función y el resultado por pantalla. """


def distancia_puntos(x1,y1,z1,x2,y2,z2):
    """float*6-->float
    OBJ:distancia entre dos puntos plano tridimensional
    PRE: Todos los valores deben de ser float"""
    import math
    distancia_puntos= math.sqrt((x1-x2)**2 +(y1-y2)**2 + (z1-z2)**2)
    
    return distancia_puntos

"""PROBADOR"""
print(distancia_puntos(1,1,1,2,2,2))#debe dar 1.732 aprox
print(distancia_puntos(0,0,0,2,2,2))#debe dar 3.464 aprox
print(distancia_puntos(4,-3,5,9,1,-25))# debe dar 30,675 aprox 

"""Una de las cosas que menos me covence de el programa es que se tenga que implementar librerias ajenas para
que la funcion funcione (como lo es math), podria resolverse utilizando un mecanismo para hacer raices cuadradas 
desde el programa."""





#Ejercicio 12 cuaderno 2 

"""12.	Los profesores solemos utilizar dos decimales cuando trabajamos con las notas parciales de un alumno,
pero en las actas se desea calificar con puntos enteros o medios (es decir: 0 / 0.5 / 1 / 1.5 /… / 9.5 /10).
Combinando operaciones y funciones enteras y en coma flotante, encuentra una fórmula general que convierta 
una nota con dos decimales a la calificación correspondiente en el acta e implementa una función que la utilice
para convertir cualquier nota. Pista (aunque te parezca obvio, esta es la pista): 0.5 (que es lo que quiero
conseguir) es la mitad de 1."""

def aproximacion(x):
    """float-->float
    OBJ: aproximar un numero para media 
    PRE: x>=0 """

    x = (x*2)
    x= round(x)
    x = (x/2)
   
    return x 

"""PROBADOR"""
print(aproximacion(8.89))
print(aproximacion(8.5))
print(aproximacion(8.45))
print(aproximacion(8.24))




# Ejercicio 13 Cuaderno 2: 
"""Haz un subprograma que determine los días, horas, minutos y segundos que hay en una 
segundos introducida por el usuario (desprecia las fracciones de segundo).
Escribe un probador para el mismo."""

def conversión (segundos):
    """float-->float*4
    OBJ: convertir segundos en días horas, minutos y segundos
    PRE: segundos>=0""" 

    días = segundos // (24 * 60 * 60)
    segundos = segundos % (24 * 60 * 60)
    horas= segundos // (60 * 60)
    segundos = segundos % (60 * 60)
    minutos = segundos // 60
    segundos = segundos % 60

    print(días,'días', horas, 'horas', minutos, 'minutos', segundos, 'segundos')


"""PROBADOR"""
print(conversión(223000))


#Ejercicio 15
"""15.	Flexibiliza el subprograma centrarRotulo de modo que el signo con el que se subraye
 y el tamaño de la ventana puedan ser distintos en diferentes ejecuciones. 
 Nota: Este ejercicio pretende enseñarte que la forma de flexibilizar un subprograma es pasarle parámetros. """

def centrarRotulo (rotulo):
    """string--> None
    OBJ: centra rótulo, subrayado con signos =, +línea encima y debajo
                    """
    tam=len(rotulo)
    if tam<72:
        lado=((72-tam)//2)-1  # 72 columnas suele ser ancho de la pantalla
        print()
        print(' '*lado,rotulo)
        print(' '*lado , '='*tam , end='\n')
    else:
        lado=((100-tam)//2)-1  #Valor mayor a 72
        print()
        print(' '*lado,rotulo)
        print(' '*lado , '*'*tam , end='\n')
        

#Probador
frase = 'Don Quijote de la Mancha'        
centrarRotulo(frase)                           # distinto nombre
centrarRotulo('Cervantes')                     # constante
rotulo = 'El famoso hidalgo don Quijote de la Mancha' # mismo nombre
centrarRotulo(rotulo)
largo ='La frase breve es más fácil de construir que la frase larga; pero el período amplio, si no se maneja muy bien'
print(centrarRotulo(largo))




#Tabla


"""	                                 David Díaz López	    David Barrientos de Marco	   Miguel Hernandez Lozano
Horas dedicadas a FP 
semana 12-18/10			                 4 horas                     2 horas                         3 horas   
Horas dedicadas a FP                     8 horas                     5 horas                         4 horas
semana 19-25/10			
David Díaz López 			                                           10                            10
David Barrientos de Marco 	               10              		                                     10
Miguel Hernandez Lozano			           10                          10
"""


"""Mis gratifiaciones personales(David Díaz) es que puedo observar como empiezo a tener una mentalidad mas logica y
como me voy adaptando al lenguaje siendo capaz de resolver problemas que antes se me hubieran hecho dificiles.""" 
