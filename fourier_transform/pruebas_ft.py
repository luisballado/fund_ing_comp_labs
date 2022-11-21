import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import sympy as smp
from skimage import color
from skimage import io
from scipy.fft import fftfreq
from scipy.fft import fft, ifft,fft2,ifft2

from scipy.integrate import quad

#t - time
#f - frequency
t,f = smp.symbols('t,f',real=True)

k = smp.symbols('k',real=True,possitive=True)

x = smp.exp(-k*t**2)*k*t

print(x)

from sympy.integrals.transforms import fourier_transform

f = np.linspace(-4, 4, 100)
x_FT = fourier_transform(x,t,f)


plt.plot(f, np.abs(x_FT))
plt.ylabel('$|\hat{x}(f)|$', fontsize=20)
plt.xlabel('$f$', fontsize=20)
plt.savefig("fourier_transform22.png")
