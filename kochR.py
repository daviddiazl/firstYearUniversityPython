import turtle

def generar_koch(level,l):
    """
    int,int-->void
    OBJ:dibujar el fractal de koch
    PRE:
    """
    if level <=0:
        turtle.forward(l)
    else:
        for grados in (60,-120,60):
            generar_koch(level-1,l/3)
            turtle.left(grados)
        generar_koch(level-1,l/3)

turtle.color('black')
generar_koch(5,500)