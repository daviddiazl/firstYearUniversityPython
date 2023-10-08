#Realizar teorema de miller 

def desc_en_2(n,b):
    """int,int-->int
    OBJ:descomponer un numero en potencias de dos
    PRE: n>2,b>=1
    """
    final = 0
    if n%2==1:
        final= n-1
    else:
        final = n
    if final/2==float:
        final = final//2 +1
    else:
        final = final//2
    return final

"""PROBADOR"""
print(desc_en_2(197,3))

def mod(x,n):
    """
    int,int-->int
    OBJ: calcular x en modulo n
    PRE:
    """
    n_mod=0
    if x<0:
        while x<0:
            x=x+n
            n_mod=x
    elif x>=0 and x<n:
        n_mod = x
    else:
        n_mod= x%n
    return n_mod


"""PROBADOR"""
print(mod(-1,2))
print(mod(1,2))
print(mod(2,2))
print(mod(3,2))

def exponen_bin(n,b,e):
    """
    int,int,int-->int
    OBJ: realizar potencia con modulo n, base b y exp e
    PRE:
    """
    sol = 1
    for i in range(15,-1,-1):
        if (e-(2**i))>=0:
            e= e-(2**i)
            sol = sol* mod(b**(2**i),n)
    return mod(sol,n)

"""PROBADOR"""
print(exponen_bin(197,3,25))









def test_miller(n,b):
    """
    int,int-->bool
    OBJ: saber si no primo
    PRE: n>2,b>=1
    """
    primo= True
    if exponen_bin(n,b,desc_en_2(n,b))!=1:
        primo = False
        for i in range(0,b):
            if exponen_bin(n,b,(2**i)*desc_en_2(n,b)) == mod(-1,n):
                primo = True
    return primo

"""Probador"""
print(test_miller(197,3))




