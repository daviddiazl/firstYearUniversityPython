"""	                                 David Díaz López	    David Barrientos de Marco	   Miguel Hernandez Lozano
Horas dedicadas a FP 
semana 12-18/10			                 4 horas                     2 horas                         3    
Horas dedicadas a FP                     8 horas                     5 horas                         4
semana 19-25/10			
David Díaz López 			                                           10                            10
David Barrientos de Marco 	               10              		                                     10
Miguel Hernandez Lozano			           10                          10
lista = [[1,2,3,4],3]
lista1 = lista
print(lista[0][3])

tupla = 9,19,24,15
tupla2 = tupla
tupla = tupla[0:2]+(7,)+tupla[3:]
print(tupla2)

jaja = ['M','B']
jaja2 = jaja
jaja = jaja[:1]
print(jaja2[2::])
print(jaja2)
print(jaja)
def e(g):		
	def a(b):		
	    r=4		
	    b=b+r		
	    return b,r		
	r=22		
	f,h=a(d)		
	h=33		
	return f		
b=3		
d=5		
g=e(d)		
print(g)	

xd= [2,4]
pb = xd 
xd[0]= 0 
xd+=[3]*2
print(pb)


pp = 7
ppa = pp
pp += 9
print(pp)


d=4 
if d!=2 and d!=4:
	print("pepe")
else:
	print(d)

for i in (60,-120,60):
	print(i)"""
grados=60
for i in range(3):
	print(grados)
	grados = -grados -60

palabra= 'pepe'
nombre = ''
for i in palabra:
	nombre+=i

print(nombre)