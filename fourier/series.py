import numpy as np
import matplotlib.pyplot as plt
from math import* 

x = np.arange(-np.pi,np.pi,0.001)
n=10

for i in range(n):
 sum=(pow(-1,i)*np.sin(i*x*(3.1416/2)))

sum = (-4/3.1416)*sum
plt.plot(x,sum,'g')

plt.title("fourier")

#plt.show()
plt.savefig("mygraph.png")
