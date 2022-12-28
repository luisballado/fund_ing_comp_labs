from scipy import signal

system = ([1.0], [1.0, 2.0, 1.0])

t,y = signal.impulse2(system)

import matplotlib.pyplot as plt
plt.plot(t,y)
plt.savefig('test.jpg')
