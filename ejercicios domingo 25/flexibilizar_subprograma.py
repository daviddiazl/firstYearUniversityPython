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
        lado=((72-tam)//2)-1  #Valor mayor a 72
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



