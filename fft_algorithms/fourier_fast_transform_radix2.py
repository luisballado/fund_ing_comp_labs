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


def FFT2(x):
    ''' radix-2 FFT '''
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

def bit_reversal(data):
    '''
    gold rader - zero padding
    :param data: array de datos
    :return: array de señal con zeros
    '''
    n = int(data.size)
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

#####################################################################
#####################################################################
#########################PROGRAMA PRINCIPAL##########################
#####################################################################
#####################################################################
parser = argparse.ArgumentParser()

parser.add_argument("-f", "--funcion", help="Ingresa la funcion a evaluar")
args = parser.parse_args()

funciones = ['pulso_rectangular','escalon_unitario','exponencial','funcion_a','funcion_b']

funcion = args.funcion

if funcion in funciones:

    #APLICAR AQUI RELLENADO DE CEROS
    N = 2**8 #longitud de la señal de entrada debe ser una potencia entera de dos
    t = np.linspace(-2, 2, N)
    T = t[1]-t[0]
    
    #switch funciones a elegir
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
    
        
    # Calcular la escala de frecuencia para graficar
    freq_scale = np.linspace(0,1/T, N)
    #print("frecuencia: " + str(1/T))
    
    # graficar los resultados
    spectrum = FFT2(signal)
    magnitude = np.absolute(spectrum)
    phase = np.angle(spectrum)

    #creacion de grafico con resultados
    f, (ax1,ax2,ax3) = plt.subplots(3, 1)
    ax1.plot(t, signal) #Señal
    ax1.set_title('Señal')
    ax2.plot(freq_scale, magnitude) #Magnitud (abs(fft))
    ax2.set_title('FFT')
    #ax3.stem(freq_scale, phase) #con rayas y puntos
    ax3.plot(freq_scale, phase) #Angulo de Fase
    ax3.set_title('Angulo de Fase')
    f.tight_layout()
    plt.savefig("fourier_transform_"+funcion+".png") #guardar imagen
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
