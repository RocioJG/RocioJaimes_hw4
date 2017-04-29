#Rocio Jaimes tarea 4
import matplotlib.pyplot as plt
import math
import numpy as np

#Leer y guardar los datos .txt generados por DifsuionTemperatura.c
t0=np.loadtxt("t0.txt")
t100=np.loadtxt("t100.txt")
t2500=np.loadtxt("t2500.txt")
tmean=np.loadtxt("tmean.txt")
#Hacer graficas (guardar sin mostrar) de las tempraturas T(t,x,y) para t=0s, 100s, 2500s para cada uno de los casos y condiciones de frontera
'''cargar tiempo en columna cero y temperatura en columna 1
'''
t0tiempo=t0[:,0]
t100tiempo=t100[:,0]
t2500tiempo=t2500[:,0]
tmeantiempo=tmean[:,0]

t0T=t0[:,1]
t100T=t100[:,1]
t2500T=t2500[:,1]
tmeanT=tmean[:,1]
#Hacer graficas para cada uno de los casos de la tempratura promedio comprarando las tres condidicones de frontera
plt.figure()
plt.plot(t0tiempo, t0T)
plt.xlabel("tiempo")
plt.ylabel("temperature")
plt.title("Temperatura vs. tiempo ecuación de difusion para t=0s")
plt.savefig('TiempoCero.pdf')

plt.figure()
plt.plot(t100tiempo, t1000T)
plt.xlabel("tiempo")
plt.ylabel("temperature")
plt.title("Temperatura vs. tiempo ecuación de difusion para t=100s")
plt.savefig('TiempoCien.pdf')

plt.figure()
plt.plot(t2500tiempo, t2500T)
plt.xlabel("tiempo")
plt.ylabel("temperature")
plt.title("Temperatura vs. tiempo ecuación de difusion para t=2500s")
plt.savefig('Tiempo2500.pdf')


#Hacer una animacion 3D de T en funcion del tiempo para el caso 1 con condiciones de frontera periodicas 



