#Ejercicio 6

"""6.	Una industria mantiene una flota de camiones para repartir productos. En cada viaje,
el conductor anota la distancia recorrida en kilómetros, los litros de gasoil utilizados,
el coste del litro de gasoil y los demás costes de mantenimiento del camión (agrupados). 
Como parte del proceso de contabilidad, el controlador necesita calcular, para cada camión y para cada viaje,
los kilómetros recorridos por litro, el coste total del viaje y el coste total por kilómetro
(incluidos los gastos de mantenimiento). 
Diseña un programa sencillo que lleve a cabo estos cálculos para un camión en un viaje."""

try:
    km = float(input('Kilometros recorridos: '))
    litros = float(input('Litros de gasoil consumidos: '))
    litro_precio = float(input('Coste del litro de gasoil: '))
    mantenimiento = float(input('Coste del mantenimiento: '))
except:
    print('Por favor escriba los valores en numerico')
else:
    km_litro = km/litros
    coste_total = litros*litro_precio+mantenimiento
    coste_km = coste_total/km

    print('Los kilometros recorridos por litro son: ',km_litro,'km/L')
    print('Los gastos totales son: ', coste_total,' Euros')
    print('Los gastos por kilometro son: ',coste_km,' Euros/km')