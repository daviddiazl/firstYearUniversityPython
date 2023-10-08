"""demo_list=[1,'hello',True,[1,2,3]] #diferentes tipos de datos
print(demo_list)

colors= ['red','blue','green']#mismo tipo
print(colors)

number_list= list((1,2,3))#otra manera de crear listas,ponerlo como tupla
print(number_list)

r= list(range(1,10))#crea una lista en un determinado rango
print(r)

print(dir(colors))#imprime cuantas operaciones se pueden hacer con listas
print(len(demo_list))#imprime la longitud de la lista
print(demo_list[1])#imprime el valor de la posicion numero uno de la lista
print('green' in colors)#para saber si hay un valor en especfico en la lista


print(colors)
colors[1]='yellow'#Los valores de las listas pueden cambiar
print(colors)

colors.append('violet')#Se pueden agregar nuevos espacios y valores(con append solo uno)
print(colors)
colors.extend(['violet','yellow'])#con extend se puede agregar mas de un valor nuevo con tuplas
print(colors)

colors.insert(1,'pink')#inserta un uevo valor en un sitio en especifico
print(colors)

colors.pop()#borra los ultimos elementos agregados
print(colors)
colors.pop(0)#borra el elemento de una posicion en especifico
print(colors)

colors.remove('green')#borra un elemento en especifico
print(colors)

print(colors.sort())#ordna los elementos
print(colors.sort(reverse=True))#Los ordena al reves

print(colors.index('red'))#Dice la posicion en la que se alla un elemento

listt=[3]
print(type(listt))"""

lista = [0,0,0,0,0,0]
for i in range(1,7):
    lista[i-1]= lista[i-1] + 1
    print(lista)