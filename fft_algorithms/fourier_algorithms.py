import sys
import argparse
import matplotlib.pyplot as plt
import numpy as np
import time
from random import randrange

#############################################################
######################### FUNCIONES #########################
#############################################################

def pulso_rectangular(t):
    '''PULSO RECTANGULAR'''
    #return 1 * (t > 0) - 1 * (t < 0)
    return 1 * (abs(t) < 0.5)
    
def escalon_unitatio(t):
    '''ESCALON UNITARIO'''
    return 1 * (t >= 0)

def exponencial(t):
    '''FUNCION EXPONENCIAL'''
    alpha = randrange(3)
    return np.exp(-alpha * t) * (t > 0)

def funcion_a(t):
    '''FUNCION A'''
    return 5+2*np.cos((2*np.pi*t)-(np.pi/2)) + 3*np.cos(4*np.pi*t)

def funcion_b(t):
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


def _FFT2_(x):
    x = np.array(x, dtype=float)
    N = int(x.size)
    n = np.log2(N)
    d = 1
    for i in range(1,int(n)):
        w = np.exp(-(1j*2*np.pi)/(2*d))
        for a in range(0,d-1):
            b = 0
            while(b<N-1):
                wa=pow(w,a)
                id1 = b+a+1
                id2 = b+d+a+1
                t_0 = x[id1] + (wa)*x[id2]
                t_1 = x[id1] - (wa)*x[id2]
                x[id1] = t_0
                x[id2] = t_1
                b = b+2*d
        
        d = 2*d
    return x

def _FFT_(x):
    g = bit_reversal(x)
    num_of_problems = 1
    problem_size = 2*len(x)
    Jtwiddle = 0
    a={}
    while (problem_size > 2):
        half_size = problem_size / 2
        for k in range(0,num_of_problems):
            JFirst = k*problem_size
            JLast = JFirst + half_size - 1
            Jtwiddle = 2*(len(x) - (len(x) / num_of_problems))

            j = JFirst
            while(j<=JLast):
                Tempr = a[j]
                Tempi = a[j+1]
                #realizamos la mariposa
                #primera operacion
                #rellenamos la parte real
                a[j] = Tempr + a[j+half_size]
                #rellenamos la parte imaginaria
                a[j+1] = Tempi + a[j+half_size+1]
                #segunda operacion
                delta = w[Jtwiddle+1] + w[Jtwiddle]
                gama =  w[Jtwiddle+1] - w[Jtwiddle]
                m1 = ((Tempr - a[j+half_size])+(Tempi - a[j+half_size + 1])) * w[Jtwiddle]
                m2 = delta * (Tempi - a[j+half_size+1])
                m3 = gama * (Tempr - a[j+half_size])
                a[j+half_size] = m1-m2
                a[j+half_size+1] = m1+m3
                Jtwiddle = Jtwiddle + 2
                j = j+2

        num_of_problems = 2 * num_of_problems
        problem_size = half_size
    return a
    
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

def bit_reversal(data):
    '''
    gold rader - zero padding
    :param data: array de datos
    :return: array de señal con zeros
    '''
    n = len(data)
    j = 0
    i = 0
    while i < n-1:
        k = n/2
        if (i<j):
            temp = data[int(i)]
            data[int(i)] = data[int(j)]
            data[int(j)] = temp
        while(k<=j):
            j = j-k
            k = k/2
        j = j+k
        i += 1        
    return data

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--funcion", help="Ingresa la funcion a evaluar")
args = parser.parse_args()

funciones = ['pulso_rectangular','escalon_unitario','exponencial','funcion_a','funcion_b']

funcion = args.funcion

if funcion in funciones:

        
    # Create a time-series signal
    #APLICAR AQUI RELLENADO DE CEROS
    N = 2**10 #longitud de la señal de entrada debe ser una potencia entera de dos
    
    t = np.linspace(-2, 2, N)
    T = t[1]-t[0]
    print(N)
    #switch funciones
    if funcion == 'pulso_rectangular':
        signal = pulso_rectangular(t)
    elif funcion == 'escalon_unitario':
        signal = escalon_unitatio(t)
    elif funcion == 'exponencial':
        signal = exponencial(t)
    elif funcion == 'funcion_a':
        signal = funcion_a(t)
    else:
        signal = funcion_b(t)

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
    #ax3.stem(freq_scale, phase)
    ax3.plot(freq_scale, phase)
    ax3.set_title('Angulo de Fase')
    f.tight_layout()
    #plt.plot
    
    plt.savefig("fourier_transform_"+funcion+".png")
    #plt.show()
    
else:
    parser.print_help(sys.stderr)
    print("Funciones Disponibles:")
    print("pulso_rectangular - para Pulso rectangular")
    print("escalon_unitario  - para Escalon unitario")
    print("exponencial       - para la Funcion Exponencial")
    print("funcion_a         - para la Funcion A")
    print("funcion_b         - para la Funcion B")
    sys.exit()
