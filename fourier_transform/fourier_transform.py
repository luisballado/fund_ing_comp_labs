import numpy as np
import math
import matplotlib.pyplot as plt

_x_ = np.linspace(-2,2,10000)

T = 4

f=[]

for i in _x_:
    w = 2*np.pi*i
    f.append(abs((2/w)*(np.cos(2*w)-np.cos(w))))

plt.plot(_x_,f,color="dodgerblue")
plt.title("Transformada de Fourier Funcion 1")
plt.savefig("trans_fourier.png")
