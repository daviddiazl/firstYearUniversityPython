""" Sucesion de fibonacci """

def fibonacciR(n):
    """ int--> int
    OBJ: calcular un numero de serie Fibonacci
    PRE: n>0 """

    if n== 0:
        p=1
    elif n== 1:
        p=1
    else:
        p = fibonacciR(n-1) + fibonacciR(n-2)
    return p

"""probador"""
print(fibonacciR(10))