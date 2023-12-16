import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 41.045, 24)
y = [-6.83, 5.30, 5.30, -6.83, 5.30, 5.30, 0, -5.19, -5.19, 6.88, -5.19, -5.19, 6.88, -5.19, -5.19, 6.88, -5.19,
     -5.19, 0, 5.12, 5.12, -6.87, 5.12, 5.12]

plt.plot(x,y, marker = 'x', c = 'black', linestyle = '--', linewidth = 0.4)
plt.axhline(y = 5.85, linestyle = '--', c = 'black')
plt.ylabel('Polarization')
plt.xlabel('Layers')
plt.show()

