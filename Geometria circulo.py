"""CALCULAR AREA DE CIRCULO""" 

PI= 3.1416

def area_circulo(r):
    """float--> float
    OBJ:Calcular area circulo mediante radio
    PRE: r>0"""
    return PI*r**2

def perimetro_circulo(r):
    """float--> float
    OBJ: Calcular oerimetro mediante radio
    PRe: r>0"""
    return 2*PI*r

#PROBADOR
print(area_circulo(3))

print(perimetro_circulo(3))
