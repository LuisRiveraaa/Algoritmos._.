Proceso Ejercicio4
	
	Definir h,m,s,mt,h2,h5,h10,g10 Como Real;
	
	Escribir "Para saber el costo del parqueadero:";
	Escribir "Escribir tiempo";
	Escribir  "Numero de horas que estuvo el carro aparcado:";
	leer h;
	Escribir  "Numero de minutos:";
	Leer m;
	Escribir  "Numero de segundos:";
	Leer s;
	
	mt=(h*60)+m+(s/60);
	h2=mt*(1500/120);
	h5=h2+(mt*(3000/180));
	h10=h5+(mt*60);
	g10=h10+(mt*92);
	Escribir "Tiempo que estubo el carro aparcado en minutos: ",mt;

	si mt<=120 Entonces

		Escribir "El valor del parqueadero en COP es: ",h2;
	SiNo
		
		si mt<=300 Entonces
			Escribir "El valor del parqueadero en COP es: ",h5;
			
		SiNo
			
			si mt<=600 Entonces
				Escribir "El valor del parqueadero en COP es: ",h10;
				
			SiNo
				
				si mt>=600 Entonces
					Escribir "El valor del parqueadero en COP es: ",g10;
					
				FinSi
			FinSi
		FinSi
	FinSi
	
FinProceso
