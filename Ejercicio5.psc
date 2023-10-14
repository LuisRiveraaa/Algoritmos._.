Proceso Ejercicio5
	
	Definir c,cd,d Como Real;
	
	Escribir "Costo del producto y descuento";
	Escribir "Escribir costo del producto";
	Leer c;
	
	
	
	si c<=100 Entonces
		d=c*0.1;
		cd=c-d;
		Escribir "El costo del producto: ",c;
		Escribir "Descuento: ",d;
		Escribir "El costo del producto+descuento: ",cd;
	SiNo
		
		si c<=200 Entonces
			d=c*0.12;
			cd=c-d;
			Escribir "El costo del producto: ",c;
			Escribir "Descuento: ",d;
			Escribir "El costo del producto+descuento: ",cd;
			
		SiNo
			
			si c>=200 Entonces
				d=c*0.15;
				cd=c-d;
				Escribir "El costo del producto: ",c;
				Escribir "Descuento: ",d;
				Escribir "El costo del producto+descuento: ",cd;
				
			FinSi
		FinSi
	FinSi
	
FinProceso
