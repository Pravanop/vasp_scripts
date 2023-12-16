import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 1000)
g0 = np.linspace(0, -5000, 1000)
smix = 2*8.314*500*((1-x)*np.log(0.5 - x/2) + x*np.log(x))
g = smix + g0
plt.plot(x, smix)
plt.plot(x, g0)
plt.plot(x, g)
plt.ylabel('Energy')
plt.xlabel('x')
plt.legend(['$S_{mix}*T$', '$G^{o}$', 'G'])
plt.show()