Proceso Ejercicio6
	
	Definir E,S como entero;
	Definir m,f Como Caracter;
	
	Escribir "Escriba su Edad:";
	Leer E;
	Escribir "Sexo Escribir: 1(masculino)";
	Escribir "Sexo Escribir: 2(femenino)";
	Leer S;
	
	si E<=16 Entonces
		Escribir "Se aplica la vacuna A";
	SiNo
		si E<=69 Entonces
			si S=2 Entonces
				Escribir "se aplica la vacuna B";
			SiNo
				si E>70 Entonces
					Escribir "Se aplica la vacuna C";
				SiNo
					Escribir "No se aplica Vacuna";
				FinSi
			FinSi
		FinSi
	FinSi

	
FinProceso
