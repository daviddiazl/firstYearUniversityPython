import turtle

def create_triangle(l,d):
    """
    int,int-->void
    OBJ: create equilateral triangle following dir(if 1 then left, if 0 then right)
    PRE: d==0 or d==1
    """
    for i in range(0,3):
        if(d==0):
            turtle.bk(l)
            turtle.right(120)
        elif(d==1):
            turtle.fd(l)
            turtle.left(120)


def create_pyramid(l,d):
    """
    
    """
    if(d==0):
        create_triangle(l/2,d)
        turtle.bk(l/2)
        create_triangle(l/2,d)
        turtle.right(-120)
        turtle.fd(l/2)
        turtle.right(-120)
        create_triangle(l/2,d)
    else:
        create_triangle(l/2,d)
        turtle.fd(l/2)
        create_triangle(l/2,d)
        turtle.left(120)
        turtle.fd(l/2)
        turtle.left(-120)
        create_triangle(l/2,d)


create_pyramid(200,1)

def sierpinskiR(level,l):
    """
    
    """
    if level<=0:
        turtle.fd(l)
    else:
        create_triangle

points
