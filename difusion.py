#Ecuacion de difusion en 2D
import matplotlib.pyplot as plt
import numpy as np

n_points=100
tiempo=2500

#primera iteracion con condiciones fijas
delta_x=1 #=delta_y
v=1 #cambio de unidades
delta_t=0.25*delta_x*delta_x/v
print(delta_t)  


Ti= np.zeros((100, 100))
for i in range(100):
	for j in range(100):
		if j<55 and j>45 and i>20 and i<40:
			Ti[i,j]=100
		else :
			Ti[i,j]=50
print(Ti)

Tf=np.zeros((100, 100))
Tf[0,0]=0.0
Tf[n_points-1, n_points-1]=0.0
Tp=Ti.copy()
def difusion(caso,frontera):
	print("hola")
#alpha=betha ose escibe el mas pequenho
	alpha=v*delta_t/delta_x #needs to be less than 1/2
	for k in range(1, tiempo):	
		for i in range(1, n_points-1):
			for j in range(1, n_points-1):		
				
				Tf[i,j]=((alpha*alpha)*((Tp[i+1, j]+Tp[i-1,j])+(Tp[i,j+1]+Tp[i,j-1])))+((1-(4*alpha))*Tp[i,j])
				
				if (frontera== "fijas") :
					Tf[:,99]=50.0
					Tf[:, 0]=50.0
					Tf[99,:]=50.0
					Tf[0, :]=50.0
				if (frontera=='abiertas'):
					Tf[:,99]=T[:,98]
					Tf[:, 0]=T[:, 1]
					Tf[99,:]=T[98,:]
					Tf[0, :]=T[1, :]
				if (frontera=='periodicas'):
					Tf[:,99]==T[:, 0]
					Tf[:, 0]==T[:,98]
					Tf[99,:]==T[0, :]
					Tf[0, :]==T[98,0]
		Tp=Tf.copy()
	return (T_final)

caso_1_fijas= difusion('caso1', 'fijas')
caso_2_fijas= difusion('caso2', 'fijas')

caso_1_abiertas=difusion('caso1', 'abiertas')
caso_2_abiertas=difusion('caso2', 'abiertas')

caso_1_periodicas=difusion('caso1', 'periodicas')
caso_2_periodicas=difusion('caso2', 'periodicas')
