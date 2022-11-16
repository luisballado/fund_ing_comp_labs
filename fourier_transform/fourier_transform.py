import numpy as np
import math
import matplotlib.pyplot as plt

_x_ = np.linspace(-2,2,10000)
f = []

#iterar para los valores de t
for i in _x_:
    w = 2*np.pi*i
    #f.append(abs((2/w)*(np.cos(2*w)-np.cos(w)))) #Funcion1
    f.append(abs((np.exp(-1j*w)*(-1j*w+np.exp(1j*w)-1))/((1j*w)*(1j*w)))) #Funcion2
    #f.append(abs((2-np.exp(-1j*w)-np.exp(-2j*w))/(1j*w))) #Funcion3
    
plt.plot(_x_,f,color="dodgerblue")
plt.title("Transformada de Fourier Funcion 3")
plt.show()
plt.savefig("trans_fourier_3.png")
