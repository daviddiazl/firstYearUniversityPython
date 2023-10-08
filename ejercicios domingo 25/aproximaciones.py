#Ejercicio 12

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




