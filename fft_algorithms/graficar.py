import matplotlib.pyplot as plt
import numpy as np
import time

def sgn(t):
    """Sign function"""
    return 1 * (t > 0) - 0 * (t < 0)

def x(t):
    return np.exp(-0.2 * t) * (t > 0)

t = np.linspace(-10, 10, 1000)

f, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, sharey=True)
plt.subplots_adjust(hspace=1)
ax1.set_ylim([-0.2, 1.2])

ax1.plot(t, sgn(t))
ax1.set_title(r'x(t)')

ax2.plot(t, x(2-t))
ax2.set_title(r'x(2 - t)')

ax3.plot(t, x(4*t))
ax3.set_title(r'x(4t)')

ax4.plot(t, x(0.25*t))
ax4.set_title(r'x(\frac{1}{4}t)')
ax4.set_xlabel('t (in s)')

plt.show()
