Algoritmo sin_titulo
	Definir nart, aum, val, res, sum, cost, des como real;
	Escribir 'Ingrese el numero de articulos';
	leer nart
Mientras nart > 0 hacer
	Para aum<-1 Hasta nart Con Paso 1 Hacer
		Escribir 'Escriba el valor del ',aum, ' producto'
		Leer val
		Si val >= 200 entonces
			des= val*0.15
			res=val - des
			Escribir 'Compras superiores a 200$ tienen un descuento del 15%!!'
			Escribir 'El costo del ',aum, ' producto es ', res
		Sino 
			Si val > 100 entonces
				des= val*0.12
				res=val - des
				Escribir 'Compras superiores a 100$ e inferiores a 200$ tienen un descuento del 12%!!'
				Escribir 'El costo del ',aum, ' producto es ', res
			SiNo
				Si val <= 100 Entonces
					des= val*0.10
					res=val - des
					Escribir 'Compras inferiores a 100$ tienen un descuento del 10%!!'
					Escribir 'El costo del ',aum, ' producto es ', res
				SiNo
					Si val < 200 Entonces
						des= val*0.12
						res=val-des
						Escribir 'Compras superiores a 100$ e inferiores a 200$ tienen un descuento del 12%!!'
						Escribir 'El costo del ',aum, ' producto es ', res	
					FinSi
				FinSi
			FinSi
		FinSi
	FinPara
	cost =(val-des)*nart;
	nart= nart - aum
FinMientras
Escribir 'El total a pagar es ', cost;

FinAlgoritmo
