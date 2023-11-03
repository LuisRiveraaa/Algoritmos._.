print("")
print("calculadora")
print("operaciones con dos numeros")
print("")
a=float(input("Ingrese el numero1: "))
b=float(input("Ingrese el numero1: "))
print("")
print("suma")
c=a+b
print(a,"+",b,"=",c)
print("")
print("resta")
d=a-b
print(a,"-",b,"=",d)
print("")
print("multiplicacion")
e=a*b
print(a,"*",b,"=",e)
print("")
print("divicion")
f=a/b
print(a,"*",b,"=",f)
print("")
print("potencia")
g=a**b
print(a,"^",b,"=",g)
print("")
print("raiz")
h=a**(1/b)
print(a,"^","1/",b,"=",h)
print("")
print("suma de potencia")
i=(a**b)+(b**a)
print(a,"^",b,"+",b,"^",a,"=",i)
print("")
print("promedio")
k=(a+b)/2
print(a,"+",b,"/2 =",k)
print("")
print("Comparacion entre a y b")
if a<b:
    print("el numero mayor es: ",b)
if b<a:
    print("el numero mayor es: ",a)
elif b==a:
    print(a,"y",b,"son iguales")

