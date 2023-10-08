foods = ['apple','banana','cheese','watermelon']

for food in foods:
    if food =='cheese':
        break#el ciclo se rompe cuando se cumple la condicion
    print(food)#food es una variable que va aumentando hasta llegar al valor total de la lista foods

for food in foods:
    if food =='cheese':
        continue#continua el ciclo cuando se cumple la condicion
    print(food)

for number in range(1,11):#Asocia a la nueva variable numbers cada numero del 1 hasta el 11
    print(number)

for letter in 'hello':
    print(letter) 


def sumar_lista(lista):
    sumatorio = 0
    for i in lista:
            sumatorio += i 
    return sumatorio

print(sumar_lista([1,2,3,4]))

piezas_eu = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
print(len(piezas_eu))
for i in range(0,len(piezas_eu)):
    print(i)