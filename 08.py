print("menu seleccion")
import math
p=math.pi

n=int(input("numero de lados de poligono regular: "))
l=float(input("longitud de los lados de la figura"))


if n==3:
    print("Area del triangulo")
    a=((l**2)*(3**0.5))/4
    print("A= ",a)
if n==4:
    print("Area del cuadrado")
    a=l*l
    print("A= ",a)
if n==5:
    teta=(2*p)/(2*n)
    ap=l/(2*math.tan(teta))
    print("Area de un pentagono")
    a=((n*l)*ap)/2
    print("A= ",a)
if n==6:
    teta=(2*p)/(2*n)
    ap=l/(2*math.tan(teta))
    print("Area de un hexagono")
    a=((n*l)*ap)/2
    print("A= ",a)
if n==7:
    teta=(2*p)/(2*n)
    ap=l/(2*math.tan(teta))
    print("Area de un heptagono")
    a=((n*l)*ap)/2
    print("A= ",a)
if n<=0:
    print("Error (area de circulo tomando lado como radio)")
    a=p*l**2
    print("A= ",a)
elif n>=8:
    print("Error (area de circulo tomando lado como radio)")
    a=p*l**2
    print("A= ",a)

