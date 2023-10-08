#Conversion de metros a Barns y viceversa 

"""El Barn es una unidad de superficie muy utilizada en la física
 de partículas, que equivale a 10-28 m². Para ilustrar su tamaño,
ten en cuenta que un Barn es, aproximadamente, el área de la 
sección transversal del núcleo de un átomo de uranio.
 Programa dos funciones, una que permita convertir unidades en m²
a Barns, y su inversa."""


def metro_barn(m):
    """ fload--> fload
    OBJ: convertir m**2 a Barns y viceversa
    PRE: m y barns = fload """

    return m*(10**-28)

def barn_metro(B):
    """ fload--> fload
    OBJ: convertir m**2 a Barns y viceversa
    PRE: m y barns = fload """

    return B/(10**-28)


"""PRUEBA"""

print(metro_barn(10**28),'Barns')
print(barn_metro(10**28), 'm^2')

