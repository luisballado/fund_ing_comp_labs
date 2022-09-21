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

import Crypto.Util.number #libreria pycriptodome
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def usuario_uno():
    print('usuario_uno executed')
    return 0

def usuario_dos(s, q, p):
    print('usuario_dos executed')
    return 0

start_time = time.time()

bits = 1024

# Obtener un num primo de N bits
# https://www.pycryptodome.org/src/util/util#module-Crypto.Util.number
P = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

print("Random n-bit Prime (p): ",P)

# Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
G = 1024

print('El valor de P es: %d'%(P))
print('El valor de G es: %d'%(G))

# numero cliente 1
cliente1 = random.randint(3, 9)

print('El valor de la llave del cliente1 es: %d',cliente1)

# Generar la llave
# Power function to return value of (G^(cliente1)) * mod P
x = int(pow(G,cliente1,P))

# numero cliente2
cliente2 = random.randint(9, 19)

print('El valor de la llave del cliente2 es: %d',cliente2)

# Power function to return value of (G^(cliente2)) * mod P
y = int(pow(G,cliente2,P))

# (y^(cliente1)) * mod P
key_cliente1 = int(pow(y,cliente1,P))

# (x^(cliente1)) * mod P
key_cliente2 = int(pow(x,cliente2,P))

print('Secret key client1 is: %d'%(key_cliente1))
print('Secret key client2 is: %d'%(key_cliente2))

security_values = [1024,1124,1224,1324]
time_executed = [3, 8, 1, 10]

# create data
x1 = np.array(security_values)
y1 = np.array(time_executed)

plt.plot(x1, y1,marker="o")

plt.title("Lab1: Diffie Hellman")
plt.xlabel("Nivel de seguridad (bits)")
plt.ylabel("Tiempo de ejecución (segundos)")



# Ejecutar 10 veces el codigo
"""
for i in range(1,11):

  print(random.getrandbits(i))
"""


print("----%s segundos ----" % (time.time() - start_time))

plt.show()