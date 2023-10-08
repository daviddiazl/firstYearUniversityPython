def lista_ordenada(lista):
    """lista-->nada
    OBJ: ordena la lista 
    PRE:"""
    for pos in range(len(lista)-1):
        menor = pos_menor(lista,pos)
        lista[pos],lista[menor] = lista[menor],lista[pos]

"""PROBADOR"""
lista_prueba = [56,33,1,9,17]
lista_ordenada(lista_prueba)
print(lista_prueba)