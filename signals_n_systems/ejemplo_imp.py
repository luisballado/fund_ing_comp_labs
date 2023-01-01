import numpy as np
import matplotlib.pyplot as plt

def u(t):
    """Unit step function"""
    return 1 * (t >= 0)

#definicion delta function
def imp(t):
    return ((t)==0)*1.0

t = np.arange(-10,10,1)
g = np.array([0])

for i in range(10):
    data = -3*i-1
    g = g + 5*imp(t+data)
    

plt.figure(0)
plt.stem(t,g)
plt.grid()
plt.savefig('example2.png')


plt.figure(1)
plt.stem(t, np.cos(t*np.pi)*u(-t-2))
plt.grid()
plt.savefig('example3.png')

plt.figure(2)
plt.stem(t, u(t+3)+0.5*u(t-1))
plt.grid()
plt.savefig('example4.png')
