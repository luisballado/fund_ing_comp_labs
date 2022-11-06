import numpy as np
import math
import matplotlib.pyplot as plt

# Setup
#La funcion numpy.linspace genera un array NumPy
#formado por n numeros equiespaciados entre dos dados.
x_ = np.linspace(-4,4,1000)

#Periodo a graficar
T = 4

#Armonicos valor de n
armonicos = 10

# Bn coefficients
def bn(n):
    n = int(n)
    #return ((-n*np.pi)*pow(-1,n))/pow(n*np.pi,2) #funcion1
    return 0 #funcion2
    #return (4*((math.sin((np.pi*n)/4))**2))/(np.pi*n)#funcion3

def an(n):
    n=int(n)
    #return (pow(-1,n)-1)/pow(n*np.pi,2) #funcion1
    return (2*((math.cos((n*np.pi)/2))))/(np.pi-(pow(n,2)*np.pi)) #funcion2
    #return 0 #funcion3
    
# Wn NO CAMBIA
def wn(n):
    global T
    wn = (2*np.pi*n)/T
    return wn

# funcion serie de fourier
def serie_fourier(armonico,x):

    #a0 = 1/2 #funcion1
    a0 = 2/np.pi #funcion2
    #a0 = 0 #funcion3
    partialSums = a0

    for n in range(1,armonico):
        try:
            partialSums = partialSums + an(n)*np.cos(wn(n)*x) + bn(n)*np.sin(wn(n)*x)
        except Exception as e:
            print(e)
            pass
        
    return partialSums

#formar el array a graficar
f = []

for i in x_:
    f.append(serie_fourier(armonicos,i))

plt.plot(x_,f,color="dodgerblue")
plt.grid()
plt.title("Serie trigonométrica con " + str(armonicos) + " terminos")
plt.savefig("mygraph.png")
