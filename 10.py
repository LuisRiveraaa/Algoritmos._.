import math as ma
#Calculadora AC
print ("""
***************************************
MENU DE SELECCION DE CIRCUITO RLC
1. Circuito en serie
2. Circuito en paralelo""")
N=int(input("SELECCIONE EL TIPO DE CIRCUITO A CALCULAR: "))
print ("""***************************************
""")


#Pedir datos
volt=int(input("Ingrese el valor de la tension RMS [V]: "))
frec=int(input("Ingrese el valor de la frecuencia [Hz]: "))
resist=int(input("Ingrese el valor de la resistencia [Ohm]: "))
induct=float(input("Ingrese el valor de la inductancia [H]: "))
capc=float(input("Ingrese el valor de la Capacitancia [microF]: "))
print ("""
***************************************
        """)

#Calculo voltajes
angvolt=0

if N==1:
#reactancia inductiva
    rinduct=2*ma.pi*frec*induct
#reactancia capacitiva
    rcapc=1/(2*ma.pi*frec*(capc*10**-6))
#impedancia
    imped=ma.sqrt(((resist)**2)+((rinduct-rcapc)**2))
    print ("Impedancia[Ohm]: ",imped,)
#angulo impedancia
    angimped=ma.atan((rinduct-rcapc)/resist)
    degangimped=ma.degrees(angimped)
    print ("Angulo de la impedancia[°]: ",degangimped,"""
           
***************************************
           """)
#intensidad de corriente
    inten=(volt/imped)
    print ("Intensidad de corriente[A]: ",inten)
#angulo intensidad de corriente
    anginten=(angvolt-angimped)
    deganginten=(ma.degrees(anginten))
    print ("Angulo de la intensidad de corriente [°]: ",deganginten,"""
           
***************************************
           """)
    
#potencia aparente 
    spot=volt*inten
    print ("Potencia aparente[Va]: ",spot)
#potencia activa
    ppot=(spot*ma.cos(angimped))
    print ("Potencia activa[W]: ",ppot)
#potencia reactiva
    qpot=(spot*ma.sin(angimped))
    print ("Potencia reactiva[Var]: ",qpot)
#factor de potencia
    fp=(ppot/spot)
    print ("Factor de potencia: ",fp)
    if fp <0:
        print ("""                Adelanto
               
***************************************
               """)
    else:
        print ("""                Atraso
               
***************************************
               """)
        
#Paralelo 
elif N==2:
    print("paralelo")
#reactancia inductiva
    rinduct=2*ma.pi*frec*induct
#reactancia capacitiva
    rcapc=1/(2*ma.pi*frec*(capc*10**-6))
#Intensidad resistencia
    intenresist=volt/resist
    print ("Intensidad en la resistencia[A]: ",intenresist)
#intencidad de la corriente 
    realin=intenresist*ma.cos(0)
    print("intensidad de la corriente =",realin)
#Angulo de intensidad de corriente en resistencia
    
    print("angulo de la intensidad de la corriente = 0ª")
#potencia aparente 
    spot=volt
    print ("Potencia aparente[Va]: ",spot)
#potencia activa
    ppot=(spot)
    print ("Potencia activa[W]: ",ppot)
#potencia reactiva
    qpot=(spot)*0
    print ("Potencia reactiva[Var]: ",qpot)
#factor de potencia
    fp=(ppot/spot)
    print ("Factor de potencia: ",fp)
    if fp <0:
        print ("""                Adelanto
               
***************************************
               """)
    else:
        print ("""                Atraso
               
***************************************
               """)
    
else:
    print ("Error")