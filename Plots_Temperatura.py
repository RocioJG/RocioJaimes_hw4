#Rocio Jaimes tarea 4
import matplotlib.pyplot as plt
import math
import numpy as np

#Leer y guardar los datos .txt generados por DifsuionTemperatura.c
T_11=np.loadtxt("11.txt")
T_12=np.loadtxt("12.txt")

T_21=np.loadtxt("21.txt")
T_22=np.loadtxt("22.txt")

T_31=np.loadtxt("31.txt")
T_32=np.loadtxt("32.txt")

x= linspace(0, 1.0, n_x)
y= linspace(0, 1.0, n_y)

mn_11=np.loadtxt("mn_11")
mn_12=np.loadtxt("mn_12")
mn_21=np.loadtxt("mn_21")
mn_22=np.loadtxt("mn_22")
mn_31=np.loadtxt("mn_31")
mn_32=np.loadtxt("mn_32")
#Hacer graficas (guardar sin mostrar) de las tempraturas T(t,x,y) para t=0s, 100s, 2500s para cada uno de los casos y condiciones de frontera
'''cargar tiempo en columna cero y temperatura en columna 1
'''
#11
fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, T_11, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura instantanea (°C)')
fig.savefig("11_2500.pdf")

#12
fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, T_12, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura instantanea (°C)')
fig.savefig("12_2500.pdf")

#21
fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, T_21, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura instantanea (°C)')
fig.savefig("21_2500.pdf")

#22
fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, T_22, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura instantanea (°C)')
fig.savefig("22_2500.pdf")

#31
fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, T_31, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura instantanea (°C)')
fig.savefig("31_2500.pdf")

#32
fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, T_32, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura instantanea (°C)')
fig.savefig("32_2500.pdf")

#Hacer graficas para cada uno de los casos de la tempratura promedio comprarando las tres condidicones de frontera

fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, mn_11, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura promedio (°C)')
fig.savefig("mn_11.pdf")

fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, mn_21, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura promedio (°C)')
fig.savefig("mn_21.pdf")

fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface( x, y, mn_31, rstride=4, cstride=4, alpha=0.25)
ax.set_title('name')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
ax.set_zlabel('Temperatura promedio (°C)')
fig.savefig("mn_31.pdf")

#Hacer una animacion 3D de T en funcion del tiempo para el caso 1 con condiciones de frontera periodicas 



