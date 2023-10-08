"""3) En las actas universitarias es necesario expresar la calificación numérica y también la textual
 según el siguiente criterio: 
0<=nota<5 suspenso, 5<=nota<7 aprobado, 7<=nota<9 notable 9<=nota<10 sobresaliente, nota=10 M. Honor. 
Haz un subprograma que reciba una calificación numérica comprendida entre 0 y 10 y devuelva la calificación textual.
Recuerda anidar los condicionales.
 """

def actas_uni(nota):
    """float--> string
    OBJ: recibir calificacion textual
    PRE: nota>=0 y nota<=10"""

    if nota <5:
        calificacion ='Suspenso'
    elif nota <7:
        calificacion = 'Aprobado'
    elif nota <9 :
        calificacion = 'Notable'
    elif nota<10:
        calificacion = 'Sobresaliente'
    else:
        calificacion = 'M. Honor'
    
    return calificacion 


"""Probador"""
print(actas_uni(2))
print(actas_uni(5))
print(actas_uni(7))
print(actas_uni(9))
print(actas_uni(10))