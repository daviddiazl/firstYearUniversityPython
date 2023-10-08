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