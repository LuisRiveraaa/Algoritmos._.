Proceso Ejercicio2
	Definir s,m,h,mt,c como real;
	
	Escribir "Para saber el costo de la llamada ingrese:";
	Escribir "Tiempo de la llamada: ";
	Escribir  "Numero de horas:";
	leer h;
	Escribir  "Numero de minutos:";
	Leer m;
	Escribir  "Numero de segundos:";
	Leer s;
	
	mt=(h*60)+m+(s/60);
	c=mt*93;
	Escribir "la duracion de la llamada en minutos: ",mt;
	Escribir "El costo total de la llamada en COP es: ",c;

FinProceso
