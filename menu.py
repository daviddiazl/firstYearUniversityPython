tFiesta=recordclass('Fiesta','dd mm dia_sem n_av')
#tAgenda= list numero_indeterminado de tFiesta, sin orden 
f1=tFiesta(17,4,'D',80)
f2= tFiesta(16,4,'S',39)
f3= tFiesta(11,4,'L',45)
a=[f1,f2,f3]
while respuesta =='a' or respuesta=='b' or respuesta=='c':
    respuesta = input('Escoja una opcion'):
    if respuesta == 'a':
    print ('a.- num fiestas totales'len(agenda))#en general no se lo que contiene la agenda
    elif respuesta=='b':
    print ('b.- num avellanas en la fiesta 1?',f1.n_av)
    elif respuesta=='c':
    print ('c.- dia de la semana de la fiesta 2', f2.dia_sem)