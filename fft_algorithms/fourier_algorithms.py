import sys
import argparse
import matplotlib.pyplot as plt
import numpy as np
import time
from random import randrange

#############################################################
######################### FUNCIONES #########################
#############################################################

def _pul_rect_(t):
    '''PULSO RECTANGULAR'''
    return 1 * (t >= 0) - 1 * (t < 0)

def _esc_unit_(t):
    '''ESCALON UNITARIO'''
    return 1 * (t >= 0)

def _exp_(t):
    '''FUNCION EXPONENCIAL'''
    alpha = randrange(3)
    return np.exp(-alpha * t) * (t > 0)

def f_A(t):
    '''FUNCION A'''
    return 5+2*np.cos((2*np.pi*t)-(np.pi/2)) + 3*np.cos(4*np.pi*t)

def f_B(t):
    '''FUNCION B'''
    return 5+8*np.cos((2*np.pi*t)-(np.pi/2))+4*np.cos(4*np.pi*t)+2*np.cos((8*np.pi*t)-(np.pi/2))+np.cos(16*np.pi*t)+2*np.cos((32*np.pi-(np.pi/2)))

#############################################################
#############################################################
#############################################################


#Funcion para acomodar fft_shift
"""
def FFT_radix2(x):
    delta = 1
    N = len(x)
    n = log2(N)
    for _pass_ in range(1,n):
        W = np.exp((-1j*2*np.pi)/2*delta)
        a = 0
        while(a < delta):
            b = 0
            while(b < N):

                t0 = x[b+a]+W
                
                
            b = b + 2*delta
        
    return None
"""

def naiveFFT(x):
    ''' The naive implementation for comparison '''
    N = x.size
    X = np.ones(N)*(0+0j)

    for k in range(N):
        A = np.ones(N)*(0+0j)
        for n in range(N):
            A[n] = x[n]*np.exp(complex(0, 2*np.pi*k*n/N))
        X[k] = sum(A)

    return X


def FFT(x):
    ''' Recursive radix-2 FFT '''
    x = np.array(x, dtype=float)
    N = int(x.size)
    
    # Use the naive version when the size is small enough
    if N <= 8:
        return naiveFFT(x)
    else:
        #Calculate first half of the W veco
        k = np.arange(N//2)
        W = np.exp(-2j*np.pi*k/N)
        evens = FFT(x[::2])
        odds = FFT(x[1::2])
        return np.concatenate([evens + (W * odds), evens - (W * odds)])
    return 0

# Create a time-series signal
N = 2**10
t = np.linspace(-10, 10, N)
T = t[1]-t[0]

#signal = rect(t)
signal = exp_func(t)

#fft = FFT(signal)
#multiplicar a -1 a los indices para ver centrado

# Calculate the frequency scale for the plot
freq_scale = np.linspace(0,1/T, N)

print("frecuencia: " + str(1/T))

# Plot the results
spectrum = FFT(signal)
magnitude = np.abs(spectrum)
phase = np.angle(spectrum)
f, (ax1,ax2,ax3) = plt.subplots(3, 1)
ax1.plot(t, signal)
ax1.set_title('Señal')
ax2.plot(freq_scale, magnitude)
#ax2.plot(freq_scale, np.absolute(fft))
ax2.set_title('FFT')
ax3.plot(freq_scale, phase)
ax3.set_title('Angulo de Fase')
f.tight_layout()
#plt.plot

#plt.savefig("fourier_transform_example.png")
plt.show()



"""
def rect(x):
    y = x
    for i in range(len(x)):
        if abs(x[i]) <= 0.5:
            y[i] = 1
        else:
            y[i] = 0
    return y

def esc_uni(x):
    y = x
    for i in range(len(x)):
        if x[i] <= 0:
            y[i] = 0
        else:
            y[i] = 1
    return y

def exp_func(x):
    y = x
    for i in range(len(x)):
        if x[i] > 0:
            y[i] = np.exp(-4*x[i])
        else:
            y[i] = 0
    return y

x = np.linspace(-2,2,1000)
y = rect(x)
plt.plot(x,y,label=r'$y=e^-4t$',color="dodgerblue")
axes = plt.gca()
axes.set_xlim([x.min(),x.max()])
axes.set_ylim([y.min(),y.max()])
plt.title('Exponential Curve')
plt.xlabel('$x$')
plt.ylabel('$\exp(x)$')
plt.legend(loc='upper left')
plt.plot
plt.show()
"""

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--funcion", help="Ingresa la funcion a evaluar")
args = parser.parse_args()

if args.funcion:
    print('Switch aca')
else:
    parser.print_help(sys.stderr)
    print("Funciones Disponibles:")
    print("pulso_rectangular - para Pulso rectangular")
    print("escalon_unitario  - para Escalon unitario")
    print("exponencial       - para la Funcion Exponencial")
    print("funcion_a         - para la Funcion A")
    print("funcion_b         - para la Funcion B")
    sys.exit()
