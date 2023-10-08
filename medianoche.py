#Ejercicio 5 

"""5.Escribe un programa que dada una hora
 (expresada en hora, minutos y segundos) muestre por pantalla
  el total de segundos transcurridos desde la última medianoche
   y los que quedan para la siguiente medianoche."""

try:
    hora= int(input('Escriba la hora actual: '))
    minuto= int(input('Escriba el minuto actual: '))
    segundo= int(input('Escriba el segundo actual: '))
except:
    print('Por favor escriba un valor numerico')
else:
    segundos_totales = hora*3600 + minuto*60 + segundo
    hasta_medianoche = 86400-segundos_totales

    print('Los segundos transcurridos desde la medianoche son: ',segundos_totales)
    print('Los segundos restantes para la medianoche son: ', hasta_medianoche)

