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
