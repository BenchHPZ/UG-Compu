import numpy as np
import matplotlib.pyplot as plt

# Devuelve un arreglo con los valores de la funcion F(k) 
# para k=0,...,n
def fncF(n):
  v = np.zeros(n+1)
  v[0] = np.log(6/5.0)
  if n==0:
    return v
  else:
    for k in range(n):
      v[k+1] = 1.0/(k+1) - 5*v[k]
    return v


n = 23
v = fncF(n)
for k in range(n+1):
  print("F(%d) = %f" % (k, v[k]))


# Integrando
def fnc_f(x, n):
  return np.power(x, n)/(5 + x)

# Generamos varias graficas del integrando, usando m puntos en
# cada una de ellas. Las m abscisas de los puntos estan en el 
# arreglo vx y son una particion uniforme del intervalo [0,1]
m  = 50
vx = np.linspace(0, 1, m)

# Creamos el arreglo vy para almacenar los valores del integrando
# evaludo en las abscisas vx
vy = np.zeros(m)

fig, ax = plt.subplots()
for n in range(5):
  for i in range(m):
    vy[i]= fnc_f(vx[i], n)
  # Para cada n, se grafica la linea poligonal que une los puntos (vx[i], vy[i])
  ax.plot(vx, vy, label="n=%d" % (n))

ax.set(xlabel='x', ylabel='f(x,n)', title='Integrando')
ax.grid()
plt.legend(loc='upper left')

# En el Notebook las instrucciones anteriores son suficientes para generar
# la grafica, pero si ejecutan el script desde linea de comandos hay que
# agregar la siguiente instruccion para ver la grafica

plt.show()