import numpy as np
import math
import matplotlib.pyplot as plt

'''
Tarea 1
@luisballado
'''

# Setup
#La funcion numpy.linspace genera un array NumPy
#formado por n numeros equiespaciados entre dos dados.
x_ = np.linspace(-2,2,1000)

#Periodo a graficar
#T=1 #funcion1
T = 4 #funcion3

#Armonicos valor de n
armonicos = 10

#Coeficiente An
def an(n):
    n=int(n)
    #return (pow(-1,n)-1)/pow(n*np.pi,2) #funcion1
    return (2*((math.cos((n*np.pi)/2))))/(np.pi-(pow(n,2)*np.pi)) #funcion2
    #return 0 #funcion3


#Coeficiente Bn
def bn(n):
    n = int(n)
    #return ((-n*np.pi)*pow(-1,n))/pow(n*np.pi,2) #funcion1
    return 0 #funcion2
    #return (4*((math.sin((np.pi*n)/4))**2))/(np.pi*n)#funcion3

    
#Wn
def wn(n):
    global T
    wn = (2*np.pi*n)/T
    return wn

#Serie de Fourier
def serie_fourier(armonico,x):

    #a0 = 1/2 #funcion1
    a0 = 2/np.pi #funcion2
    #a0 = 0 #funcion3
    sumas = a0

    for n in range(1,armonico):
        try:
            #sumas = sumas + an(n)*np.cos(wn(n)*x) + bn(n)*np.sin(wn(n)*x)
            sumas = sumas + (6/wn(n))*np.sin(2*wn(n))
        except Exception as e:
            print(e)
            pass
        
    return sumas

#formar el array a graficar
f = []

for i in x_:
    f.append(serie_fourier(armonicos,i))

plt.plot(x_,f,color="dodgerblue")
plt.grid()
plt.title("Serie trigonométrica con " + str(armonicos) + " terminos")
plt.savefig("trabs_fourier.png")
