"""
Implementar un programa que realice lo siguiente:

1. Debe recibir como entrada un numero primo p, de cualquier tamaño (por ejemplo los recomendados para aplicaciones criptograficas (1024,2048))

2. Construir un Grupo Multiplicativo Zp* (usando el conjunto {1,2...p-1}) y la operación * mod p

3. Usar como generador, algun elemento aleatorio de Zp*

4. Ejecutar el protocolo Diffie Hellman. Se deberá verificar que tanto el valor calculado en A como en B son iguales.

5. Se deberá ejecutar en al menos 10 casos de prueba, usando un valor de p diferente para cada caso, siendo que p puede ser de entre 1024 y 2048 bits.

6. Reportar una tabla de tiempos de ejecución para cada caso de prueba.
  1. EjeX: Nivel de seguridad (tamaño de bits de p)
  2. EjeY: Tiempo de ejecución del protocolo Diffie Hellman
"""

import Crypto.Util.number  #libreria pycriptodome
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import statistics
from tabulate import tabulate

"""
Clase Usuario Uno
"""
class UsuarioUno:

    def __init__(self, G, P):
        self.g = G
        self.p = P
        self.a = 17

    def __generator__(self):
        self.x = int(pow(self.g, self.a, self.p))

        return self.x

    def __make_key__(self, y):
        self.usuario_uno_key = int(pow(y, self.a, self.p))

        return self.usuario_uno_key


"""
Clase Usuario Dos
"""
class UsuarioDos:

    def __init__(self, G, P):
        self.g = G
        self.p = P
        self.b = 15

    def __generator__(self):
        self.y = int(pow(self.g, self.b, self.p))
        return self.y

    def __make_key__(self, x):
        self.usuario_dos_key = int(pow(x, self.b, self.p))
        return self.usuario_dos_key


# Input _bits_
def diffie_hellman(_bits_):
    P = Crypto.Util.number.getPrime(_bits_,
                                    randfunc=Crypto.Random.get_random_bytes)
    G = (random.randint(1, P - 1)) % P

    cliente1 = UsuarioUno(G, P)
    x = cliente1.__generator__()

    cliente2 = UsuarioDos(G, P)
    y = cliente2.__generator__()

    #print("El valor de X es: " + str(x))
    #print("El valor de Y es: " + str(y))

    key_cliente1 = cliente1.__make_key__(y)
    key_cliente2 = cliente2.__make_key__(x)

    print("LLAVE_CLIENTE1: " + str(key_cliente1))
    print("LLAVE_CLIENTE2: " + str(key_cliente2))

def graficar(x_datos,y_datos,result_arr):

  
  print(tabulate(result_arr))
  
  x1 = np.array(x_datos)
  y1 = np.array(y_datos)
  
  plt.plot(x1, y1, marker="o")
  
  plt.title("Lab1: Diffie Hellman")
  plt.xlabel("Nivel de seguridad (bits)")
  plt.ylabel("Tiempo de ejecución (segundos)")
  plt.grid()
  plt.show()
  


#bits = [1024, 1128, 1232, 1336, 1440, 1544, 1648, 1752, 1856, 1960, 2048]

bits = [1024,1128,1232,1336,1440,1544,1648,1752,1856,1960,2048]
time_cicle = []
time_mean = []
_result_arr_ = []

for i_bits in bits:
    _bits_arr_ = []
    _bits_arr_.append("Bits")
    _bits_arr_.append(i_bits)
    start_time_cicle = time.time()

    for i in range(10):

        print("__::ronda::__" + str(i))
        diffie_hellman(i_bits)
        time_cicle.append(time.time() - start_time_cicle)
      
    mean = statistics.mean(time_cicle)
  
    _bits_arr_.append(mean)
    time_mean.append(mean)
    _result_arr_.append(_bits_arr_)


# create data
graficar(bits,time_mean,_result_arr_)