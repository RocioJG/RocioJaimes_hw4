#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define PI 3.1415

FILE *output;

int main()
{
int tiempo=2500;
double delta_x=1.0;
double v=1.0;
int filas=100;
int columnas=100;
double delta_t=0.25*delta_x*delta_x/v;
double alpha= v*delta_t/delta_x;

double Ti[filas][columnas];
double Tf[filas][columnas];
double Tp[filas][columnas];
/*creo matriz inicial*/
for (int i=1; i>filas; i++)
{	for (int j=1; j>columnas; j++)
	{
		if(i>=45 && j<=55 && i>=20 && i<=40)
			Ti[i][j]=100;
		else
			Ti[i][j]=50;
		Tp[i][j]=Ti[i][j];
	}
}
/*creo matriz final. La inicializo en ceros para detectar errores*/
for (int i=1; i>filas; i++)
{	for (int j; j>columnas; j++)
	{
		Tf[i][j]=0;
		Tmean[i][j]=0;
	}
}


/*resulevo. Itero en timepo, luego en filas y luego en columnas*/
double difusion(int frontera; int caso, double Tf[filas][columnas])
{
	double Tf;
	for (int k=1; k<2500; k++)
	{
		for (int i=1; i<100; i++)
		{
			for (int j=1; j<100; j++)
			{
				Tf[i][j]=((alpha*alpha)*((Tp[i+1][j]+Tp[i-1][j])+(Tp[i][j+1]+Tp[i][j-1])))+((1-(4*alpha))*Tp[i][j]);
				if frontera== 1
                    			if caso==1
                       				Tf[:][99]=50.0;
                        			Tf[:][0]=50.0;
                        			Tf[99][:]=50.0;
			                        Tf[0][:]=50.0;
						Tmean=Tf[:][:]/10000;
						if k==0
							
                	    		else
			                        for f in range(45,55)
						{
                			        	for c in range(20,40)
							{
		                        			Tf[f][c]=100.0;
					                        Tf[:][99]=50.0;
		                			        Tf[:][0]=50.0;
					                        Tf[99][:]=50.0;
		                			        Tf[0][:]=50.0;
								Tmean=Tf[:][:]/10000;
							}
						}
				else if (frontera== 2)
                    			if caso== 1
						Tf[:][99]=Tf[:][98];
						Tf[:][0]=Tf[:][1];
						Tf[99][:]=Tf[98][:];
						Tf[0][:]=Tf[1][:];
						Tmean=Tf[:][:]/10000;
					else 
				        	for f in range(45,55)
						{
				            		for c in range(20,40)
							{
								Tf[f][c]=100.0;
								Tf[:][99]=Tf[:][98];
								Tf[:][0]=Tf[:][1];
								Tf[99][:]=Tf[98][:];
								Tf[0][:]=Tf[1][:];
								Tmean=Tf[:][:]/10000;
							}
						}
				else
					if caso== 1
						Tf[:,99]==Tf[:, 1];
						Tf[:, 0]==Tf[:,98];
						Tf[99,:]==Tf[0, :];
						Tf[0, :]==Tf[98,0];
						Tmean=Tf[:][:]/10000;
					else
					        for f in range(45,55)
						{
							for c in range(20,40)
							{
								Tf[f][c]=100.0;
				        		        Tf[:][99]==Tf[:][ 1];
				        		        Tf[:][0]==Tf[:][98];
				        		        Tf[99][:]==Tf[0][:];
				        		        Tf[0][:]==Tf[98][0];
								Tmean=Tf[:][:]/10000; 
							}    
						}                         	
			}
		}
	}
	return Tf, Tmean;
}

/*Condiciones fijas*/
double caso_1_fijas= difusion(1, 1);
double caso_2_fijas= difusion(1, 2);

/*Condiciones periódicas*/
double caso_1_abiertas= difusion(2, 1);
double caso_2_abiertas= difusion(2, 2);

/*Condiciones abiertas*/
double caso_1_periodicas= difusion(3, 1);
double caso_2_periodicas= difusion(3, 2);
}
