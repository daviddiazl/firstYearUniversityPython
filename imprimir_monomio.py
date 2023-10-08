"""Cuaderno de trabajo 3 ejercicio 7"""

"""Hacer subprograma para imprimir monomio"""
def imprimir_monomio(coef,exp):
    """float,int-->nada
    OBJ: imprimir monomio con coeficiente y exponente
    PRE: 0<=exp""" #PRE dada por el enunciado
    if coef ==0 or exp ==0:
        print('')
    elif coef == 1 and exp ==1:
        print('x')
    elif coef ==1 and exp >1:
        print('x^',exp)
    elif coef!=0 and coef!=1 and exp ==1:
        print(coef,'x')
    else:
        print(coef,'x^',exp)

"""PROBADOR"""
imprimir_monomio(0,0)
imprimir_monomio(1.0,1)
imprimir_monomio(1.0,2)
imprimir_monomio(0.5,1)
imprimir_monomio(2.0,2)
